from .save_string import SaveString
from .print_string import PrintString
from .tokenizer_vocab import TokenizerVocab
from .pick_item_json import PickItemJson

NODE_CLASS_MAPPINGS = {
    "SaveString": SaveString,
    "TokenizerVocab": TokenizerVocab,
    "PickItemJson": PickItemJson,
    "PrintString": PrintString,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "SaveString": "IW SaveString",
    "TokenizerVocab": "IW TokenizerVocab",
    "PickItemJson": "IW PickItemJson",
    "PrintString": "IW PrintString",
}

