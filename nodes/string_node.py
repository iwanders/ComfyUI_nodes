import os
import json

class StringNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input": ("STRING",{"defaultInput": False, "default": "", "multiline": True, "dynamicPrompts": False}),
            },
            "optional": {
            },
        }

    RETURN_TYPES = ("STRING", )
    FUNCTION = "execute"

    CATEGORY = "iw"

    def execute(self, input):
        return (input,)
