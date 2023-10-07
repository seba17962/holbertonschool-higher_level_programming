#!/usr/bin/python3

def write_file(filename="", text=""):
    
    if filename is not None and filename:
        with open(filename, 'w', encoding="utf-8") as f:
            if text is not None:
                num_chars = f.write(text)
            return num_chars
