#!/usr/bin/python3
"""module that prints 2 new lines before ?, . and :"""


def text_indentation(text):
    """2 new lines after each of these characters: ., ? and :

    Args:
        text: text to print

    Returns:
        None
    """
    i = 0

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text is None or text == "":
        return

    while text[i] == ' ':
        i += 1

    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("{:s}\n".format(text[i]))
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print("{:s}".format(text[i]), end='')
            i += 1
