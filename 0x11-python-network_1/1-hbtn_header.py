#!/usr/bin/python3
'''Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found
in the header of the response'''
import sys
import urllib.request


with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.info().get('X-Request-Id')
print(html)
