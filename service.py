import os
import subprocess
from rich import print

from utils import remove_punctuation, read_text, read_csv


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


def export_file(file_path: str, text: str, file_name: str=None, start_file=True):
    """
    Export the text into a .txt file with the suffix of _replaced
    in the same folder.
    :param file_path: Path of the file to export
    :param text: Text to export
    """
    if not file_name:
        name, ext = file_path.split(".")
        file_name = name +"_replaced." + ext
    else:
        file_name += ".txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(text)
        print(
            ":rocket::rocket: Your [blue]file[/blue] has been exported! :rocket::rocket:"
        )
    if start_file:
        open_file(file_name)


def open_file(file_path: str) -> None:
    try:
        os.startfile(file_path)
    except AttributeError:
        subprocess.run(["open", file_path])


def replace_text_from_csv(csv_path: str, template_path: str, char: str, index: int = 0) -> None:
    """
    Replace the text in the file with the values in the csv file.
    :param csv_path: Path of the csv file
    :param template_path: Path of the .txt template
    :param char: Character to search in the template
    :param index: Column number to form the output file name
    """
    for i, line in enumerate(read_csv(csv_path)):
        try:
            sufix = remove_punctuation(line[index])
            if i != 0: # Skipping the csv header
                new_text = replace_text(template_path, line, char)
                export_file(template_path, new_text, "message_"+ sufix, False)
        except IndexError:
            raise ValueError(f"Index out of range. Pick one from: 1 to {len(line)}")
