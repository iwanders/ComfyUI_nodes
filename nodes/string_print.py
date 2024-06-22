
class StringPrint:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input": ("STRING", { "multiline": False, "default": "ComfyUI", "dynamicPrompts": False, "defaultInput": True}),
                "prefix": ("STRING", { "multiline": False, "default": "PrintString", "dynamicPrompts": False}),
            },
            "optional": {
            },
        }

    OUTPUT_NODE = True
    RETURN_TYPES = tuple()
    FUNCTION = "execute"
    CATEGORY = "iw"

    def execute(self, input, prefix):
        print(f"{prefix}: {input}")
        return tuple()
