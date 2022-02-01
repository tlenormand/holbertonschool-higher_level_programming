#!/usr/bin/python3
"""module that that adds all arguments to a Python list,"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    file = load_from_json_file("add_item.json")
except Exception:
    file = []

if len(sys.argv) >= 2:
    for lenght in range(1, len(sys.argv)):
        file.append(sys.argv[lenght])

save_to_json_file(file, "add_item.json")
