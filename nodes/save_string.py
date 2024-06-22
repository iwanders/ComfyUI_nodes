import folder_paths
import os
import json

class SaveString:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "filename_prefix": ("STRING", { "multiline": False, "default": "ComfyUI"}),
                "filename_suffix": ("STRING", { "multiline": False, "default": ""}),
                "string_field": ("STRING", {"multiline": True, "dynamicPrompts": True, "defaultInput": True}),
                "extension": (["txt", "json"], {"default": "txt"})
            },
            "optional": {
            },
        }

    OUTPUT_NODE = True
    RETURN_TYPES = tuple()

    FUNCTION = "execute"

    CATEGORY = "iw"

    def execute(self, string_field, filename_prefix, filename_suffix, extension):
        full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(filename_prefix, self.output_dir)
        file = f"{filename}_{counter:05}_{filename_suffix}.{extension}"
        path = os.path.join(full_output_folder, file)

        if extension == "json":
            string_field = json.dumps(json.loads(string_field), indent=4)

        with open(path, "w") as f:
            f.write(string_field)
        return tuple()
