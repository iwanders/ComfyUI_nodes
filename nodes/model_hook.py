import torch

# Trying to implement https://huggingface.co/blog/TimothyAlexisVass/explaining-the-sdxl-latent-space

# Shrinking towards the mean (will also remove outliers)
def soft_clamp_tensor(input_tensor, threshold=3.5, boundary=4):
    if max(abs(input_tensor.max()), abs(input_tensor.min())) < 4:
        return input_tensor
    channel_dim = 1

    max_vals = input_tensor.max(channel_dim, keepdim=True)[0]
    max_replace = ((input_tensor - threshold) / (max_vals - threshold)) * (boundary - threshold) + threshold
    over_mask = (input_tensor > threshold)

    min_vals = input_tensor.min(channel_dim, keepdim=True)[0]
    min_replace = ((input_tensor + threshold) / (min_vals + threshold)) * (-boundary + threshold) - threshold
    under_mask = (input_tensor < -threshold)

    return torch.where(over_mask, max_replace, torch.where(under_mask, min_replace, input_tensor))

# Center tensor (balance colors)
def center_tensor(input_tensor, channel_shift=1, full_shift=1, channels=[0, 1, 2, 3]):
    for channel in channels:
        input_tensor[0, channel] -= input_tensor[0, channel].mean() * channel_shift
    return input_tensor - input_tensor.mean() * full_shift

# Maximize/normalize tensor
def maximize_tensor(input_tensor, boundary=4, channels=[0, 1, 2]):
    min_val = input_tensor.min()
    max_val = input_tensor.max()

    normalization_factor = boundary / max(abs(min_val), abs(max_val))
    input_tensor[0, channels] *= normalization_factor

    return input_tensor

class ModelHook:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",{"defaultInput": True}),
            },
            "optional": {
            },
        }

    RETURN_TYPES = ("MODEL", )
    FUNCTION = "execute"

    CATEGORY = "iw"

    def execute(self, model):
        counter = 0;
        def cfg_hook_printer(cbk):
            nonlocal counter
            counter += 1
            timestep = (counter / 40)*1000.0
            if timestep > 950:
                threshold = max(cbk["denoised"].max(), abs(cbk["denoised"].min())) * 0.998
                cbk["denoised"] = soft_clamp_tensor(cbk["denoised"], threshold*0.998, threshold)
            if timestep > 700:
                cbk["denoised"] = center_tensor(cbk["denoised"], 0.8, 0.8)
            if timestep > 1 and timestep < 100:
                cbk["denoised"] = center_tensor(cbk["denoised"], 0.6, 1.0)
                cbk["denoised"] = maximize_tensor(cbk["denoised"])

            return cbk["denoised"]
        model.set_model_sampler_post_cfg_function(cfg_hook_printer)
        return (model,)
