import string
import csv


def remove_punctuation(text: str) -> str:
    """
    Removes punctuation from a string.
    :param text: The string to remove punctuation from.
    """
    if not text:
        return text
    else:
        translator = str.maketrans("", "", string.punctuation)
        return text.translate(translator).strip()


def read_text(file_path: str):
    """
    Read a file and return it line by line
    using generator.
    :param file_path: The path to the file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            yield line


def read_csv(file_path: str):
    """
    Read a csv file and yield each row of the csv file.
    :param file_path: The path to the csv file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            yield row
