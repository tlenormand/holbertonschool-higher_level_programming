#!/usr/bin/python3
'''Python script that takes in a URL, sends a request to the URL'''
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.info().get('X-Request-Id')
print(html)
