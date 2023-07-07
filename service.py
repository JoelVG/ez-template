import os
import subprocess
from rich import print

from utils import remove_punctuation, read_text


def replace_text(file_path: str, new_values: list, char: str) -> str:
    new_values.reverse()
    final_text = ""
    for line in read_text(file_path):
        if line:
            # Getting the words of the target words in the original text line by line
            target_words = [
                remove_punctuation(word)
                for word in line.split(" ")
                if word.startswith(char)
            ]
            if target_words:
                for word in target_words:
                    # Replacing the target word with the new value
                    line = line.replace(word, new_values.pop())
                    if char not in line:
                        final_text += line
            else:
                final_text += line
    return final_text


def export_file(file_path: str, text: str):
    """
    Export the text into a .txt file with the suffix of _replaced
    in the same folder.
    :param file_path: Path of the file to export
    :param text: Text to export
    """
    name, ext = file_path.split(".")
    new_file = name + "_replaced." + ext
    with open(new_file, "w", encoding="utf-8") as file:
        file.write(text)
        print(
            ":rocket::rocket: Your [blue]file[/blue] has been exported! :rocket::rocket:"
        )
    open_file(new_file)


def open_file(file_path: str) -> None:
    try:
        os.startfile(file_path)
    except AttributeError:
        subprocess.run(["open", file_path])


def replace_text_from_csv(csv_path: str, char: str) -> None:
    """
    Replace the text in the file with the values in the csv file.
    :param csv_path: Path of the csv file
    :param char: Character to search in the file
    """
    values = []
    with open(csv_path, "r") as file:
        for line in file:
            values.append(line.strip())
    file_path = input("Enter the path of the file to replace: ")
    text = replace_text(file_path, values, char)
    export_file(file_path, text)
