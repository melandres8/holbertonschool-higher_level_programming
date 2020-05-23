#!/usr/bin/python3
"""
    Handling new lines, some special characters
    and tabs function.
"""


def text_indentation(text):
    """
        Print a text with two new line at the end
        after each of these characters '.'':''?'

        Args:
            text: (string) Given text
        Raises:
            TypeError: "text must be a string"
    """

    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    string = ""
    for i in text:
        if i == '\n':
            pass
        else:
            string += i
        if i in '.:?':
            string = string.strip(" ")
            print(string, end="")
            print("\n")
            string = ""
    string = string.strip(" ")
    print(string, end="")
