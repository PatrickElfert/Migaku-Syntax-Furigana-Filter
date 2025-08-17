from anki import hooks
from .parser import parse_migaku_syntax
import sys
from aqt.utils import showInfo

FILTER_NAME = "migakuFurigana"

def on_field_filter(field_text: str, field_name: str, filter_name: str, context):
    if filter_name != FILTER_NAME:
        return field_text

    result = parse_migaku_syntax(field_text)     

    return result
    

hooks.field_filter.append(on_field_filter)