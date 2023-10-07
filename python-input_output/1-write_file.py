#!/usr/bin/python3
"""_summary_
"""


def write_file(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """
    if filename is not None and filename:
        with open(filename, 'w', encoding="utf-8") as f:
            if text is not None:
                return f.write(text)
