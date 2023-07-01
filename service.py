import os
from rich import print

from utils import remove_punctuation


def read_text(file_path: str):
    """
    Read a file and return it line by line
    using generator.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            yield line


def replace_text(file_path: str, new_values: list, char: str) -> str:
    new_values.reverse()
    final_text = ""
    for line in read_text(file_path):
        if line:
            # Getting the indexes of the target words in the original text line by line
            target_words = [remove_punctuation(word) for word in line.split(" ") if word.startswith(char)]
            if target_words:
                for word in target_words:
                    # Replacing the target word with the new value
                    new_line = line.replace(word, new_values.pop())
                    final_text += new_line + "\n"
            else:
                final_text += line
    return final_text


def export_file(file_path: str, text: str):
    name, ext = file_path.split(".")
    new_file = name + "_new." + ext
    with open(new_file, "w") as file:
        file.write(text)
        print(f":rocket::rocket: Your [blue]file[/blue] has been exported! :rocket::rocket:")
    os.system(new_file)
