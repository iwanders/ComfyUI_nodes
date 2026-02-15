import os
import json
from collections import deque
 
from server import PromptServer 
from aiohttp import web
import aiohttp

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "127.0.0.1:11434")


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

@PromptServer.instance.routes.get("/iw/api/ollama/models")
async def retrieve_models(request):
    print("/iw/api/ollama/models")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://{OLLAMA_HOST}/api/tags') as response:
                body = await response.json()
                model_simple = [v["model"] for v in body["models"]]
                return web.json_response({"status": "success", "models": model_simple}, status=200)
    except aiohttp.client_exceptions.ClientConnectorError as e:
        return web.json_response({"status": "success", "models": ["ollama is down"]}, status=200)
        

    return web.json_response({"status": "fail"}, status=500)
