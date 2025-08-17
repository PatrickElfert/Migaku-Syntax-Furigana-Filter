import re

def parse_migaku_syntax(text: str) -> str:
    text = re.sub(r"</?t[^>]*>", "", text)
    
    pattern = re.compile(r"([^\s\[\]]+)\[([^\]]+)\]")

    def replacer(match: re.Match[str]) -> str:
        base = match.group(1)
        reading_full = match.group(2)
        primary_reading = reading_full.split(";")[0].split(",")[0]
        return f"<ruby>{base}<rt>{primary_reading}</rt></ruby>" if primary_reading else base

    processed_text = pattern.sub(replacer, text)

    final_text = re.sub(r"\{[^}]*\}", "", processed_text)

    return final_text
