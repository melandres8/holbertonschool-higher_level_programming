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
    """

    if (not isinstance(text, str) or len(text) < 1
            or text is None):
        raise TypeError("text must be a string")
    case = False
    for item in text:
        if item in ':.?':
            print(item, end="\n\n")
            case = True
        else:
            if case is False:
                print(item, end="")
            else:
                if item in ' \t':
                    pass
                else:
                    print(item, end='')
                    case = False
