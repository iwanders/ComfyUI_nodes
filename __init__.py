from .save_string import SaveString
from .tokenizer_vocab import TokenizerVocab

NODE_CLASS_MAPPINGS = {
    "SaveString": SaveString,
    "TokenizerVocab": TokenizerVocab,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "SaveString": "IW SaveString",
    "TokenizerVocab": "IW TokenizerVocab"
}

