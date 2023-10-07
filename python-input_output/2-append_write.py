#!/usr/bin/python3
"""_summary_
"""


def append_write(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    if filename is not None and filename:
        with open(filename, 'a', encoding="utf-8") as f:
            if text is not None:
                return f.write(text)
