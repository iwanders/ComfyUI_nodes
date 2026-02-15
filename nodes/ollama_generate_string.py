import os
import json
from collections import deque
 
from server import PromptServer
class OllamaGenerateString :
    def __init__(self): 
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "int_value": ("INT",{"defaultInput": True}),
                "prompt": ("STRING",{"defaultInput": True, "default": "", "multiline": True, "dynamicPrompts": False}),
            },
            "optional": {
            },
        }

    RETURN_TYPES = ("STRING", )
    FUNCTION = "execute"
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "iw"

    @classmethod
    def IS_CHANGED(cls, int_value, prompt ): 
        return "foo"


    def execute(self, int_value, prompt): 
        result = (prompt,)
        print("Executing with ", prompt)
        print("  generating new with ", int_value)
        return { "ui": { "next_int": [int_value], "next_value": [f"super cool: {int_value}"]}, "result": [result] } 

@PromptServer.instance.routes.get("/iw/api/ollama_generate")
async def load_drawing(request):
    print("/iw/api/ollama_generate") 
