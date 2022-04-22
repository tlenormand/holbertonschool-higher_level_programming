#!/usr/bin/python3
'''Python script that sends a request to the URL'''
import sys
import requests


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code:", res.status_code)
    else:
        print(res.text)
