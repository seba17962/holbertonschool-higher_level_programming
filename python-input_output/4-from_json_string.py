#!/usr/bin/python3
"""_summary_
"""
import json


def from_json_string(my_str):
    with open(my_str, "r", encoding="utf-8") as f:
        return json.load(f)
