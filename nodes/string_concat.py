import os
import json

class StringConcat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prefix": ("STRING",{"defaultInput": True, "default": "", "multiline": True, "dynamicPrompts": False}),
                "suffix": ("STRING",{"defaultInput": True, "default": "", "multiline": True, "dynamicPrompts": False, "hidden": True}),
            },
            "optional": {
            },
        }

    RETURN_TYPES = ("STRING", )
    FUNCTION = "execute"

    CATEGORY = "iw"

    def execute(self, prefix, suffix):
        return (prefix + suffix,)
