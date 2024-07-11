from .nodes.string_save import StringSave
from .nodes.string_print import StringPrint
from .nodes.string_replace import StringReplace
from .nodes.string_node import StringNode
from .nodes.string_concat import StringConcat
from .nodes.string_from_int import StringFromInt

from .nodes.tokenizer_vocab import TokenizerVocab

from .nodes.json_pick_item import JsonPickItem

from .nodes.model_hook import ModelHook

NODE_CLASS_MAPPINGS = {
    "IW_StringSave": StringSave,
    "IW_StringPrint": StringPrint,
    "IW_StringReplace": StringReplace,
    "IW_StringNode": StringNode,
    "IW_StringConcat": StringConcat,
    "IW_StringFromInt": StringFromInt,

    "IW_TokenizerVocab": TokenizerVocab,

    "IW_JsonPickItem": JsonPickItem,

    "IW_ModelHook": ModelHook,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "IW_StringSave": "IW SaveString",
    "IW_StringPrint": "IW PrintString",
    "IW_StringReplace": "IW ReplaceString",
    "IW_StringNode": "IW StringNode",
    "IW_StringConcat": "IW StringConcat",
    "IW_StringFromInt": "IW StringFromInt",

    "IW_TokenizerVocab": "IW TokenizerVocab",

    "IW_JsonPickItem": "IW JsonPickItem",

    "IW_ModelHook": "IW ModelHook",
}

