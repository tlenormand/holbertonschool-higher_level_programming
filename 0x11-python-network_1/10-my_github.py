#!/usr/bin/python3
'''Python script that sends a request to the URL'''
import sys
import requests


if __name__ == "__main__":
    res = requests.get(
        'https://api.github.com/user',
        auth=(sys.argv[1], sys.argv[2])
    )
    print(res.json().get("id"))
