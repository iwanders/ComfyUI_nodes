import os
import json

class ReplaceString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "haystack": ("STRING",{"defaultInput": True, "default": "{}", "multiline": True}),
                "needle": ("STRING",{"defaultInput": False, "default": "%REPLACE%", "dynamicPrompts": False}),
                "value": ("STRING",{"defaultInput": True, "default": "", "dynamicPrompts": False}),
                "input_type": (["json", "verbatim"], {"default": "verbatim"}),
            },
            "optional": {
            },
        }

    RETURN_TYPES = ("STRING", )
    FUNCTION = "execute"

    CATEGORY = "iw"

    def execute(self, haystack, needle, value, input_type):
        if input_type == "json":
            z = json.loads(value)
            if type(z) is str:
                value = z
            if type(z) is list:
                value = " ".join(z)
        return (haystack.replace(needle, value),)
