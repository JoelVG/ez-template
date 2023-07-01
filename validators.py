import os

from rich import print

MARKS = ("ǂ", "ƺ", "ȡ")

def validate_file_path(path: str):    
    if os.path.isfile(path):
        return path
    else:
        raise FileNotFoundError
    
def validate_new_values(values: str):
    if "," in values:
        return values.split(",")
    return [values]

def validate_char(char: str) -> str:
    if char in MARKS:
        return char
    else:
        raise ValueError(f"Invalid character. Please set up your template using these characters: {MARKS}")
