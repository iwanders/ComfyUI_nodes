import folder_paths
from comfy import sdxl_clip
import os
import json

class TokenizerVocab:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "clip": ("CLIP",),
            },
            "optional": {
            },
        }

    OUTPUT_NODE = False
    RETURN_TYPES = ("STRING", )

    FUNCTION = "execute"

    CATEGORY = "iw"

    def execute(self, clip):
        tokenizer = clip.tokenizer
        vocab = {}
        # Is clip l and g different?
        if isinstance(tokenizer, sdxl_clip.SDXLTokenizer):
            clip_l_tokenizer = tokenizer.clip_l.tokenizer
            vocab = clip_l_tokenizer.get_vocab()

        return (json.dumps(vocab),)
