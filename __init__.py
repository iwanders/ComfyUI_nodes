from .nodes.save_string import SaveString
from .nodes.print_string import PrintString
from .nodes.replace_string import ReplaceString
from .nodes.tokenizer_vocab import TokenizerVocab
from .nodes.pick_item_json import PickItemJson

NODE_CLASS_MAPPINGS = {
    "IW_SaveString": SaveString,
    "IW_PrintString": PrintString,
    "IW_ReplaceString": ReplaceString,
    "IW_TokenizerVocab": TokenizerVocab,
    "IW_PickItemJson": PickItemJson,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "IW_SaveString": "IW SaveString",
    "IW_TokenizerVocab": "IW TokenizerVocab",
    "IW_PickItemJson": "IW PickItemJson",
    "IW_PrintString": "IW PrintString",
    "IW_ReplaceString": "IW ReplaceString",
}

