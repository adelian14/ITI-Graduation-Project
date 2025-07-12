import re
import json

def extract_json_from_text(text: str):
    """
    Extracts the first JSON object from the input string.
    Returns a Python dict.
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in the text.")

    json_str = match.group()
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON decode error: {e}\nExtracted:\n{json_str}")

def dump_clean_json(text: str, cleaned_path: str):
    """
    Extracts JSON from a string and dumps it to a new file.
    """
    data = extract_json_from_text(text)
    with open(cleaned_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return cleaned_path
