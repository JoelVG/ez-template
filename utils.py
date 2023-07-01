import string

def remove_punctuation(text: str) -> str:
    """
    Removes punctuation from a string.
    :param text: The string to remove punctuation from.
    :return: The string with punctuation removed.
    """
    if not text:
        return text
    else:
        translator = str.maketrans("", "", string.punctuation)
        return text.translate(translator)
