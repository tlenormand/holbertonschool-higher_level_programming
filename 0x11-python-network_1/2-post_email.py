#!/usr/bin/python3
'''Python script that sends a POST request to the passed URL'''
import sys
import urllib.request


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode('utf-8')

    with urllib.request.urlopen(sys.argv[1], data) as response:
        html = response.info()

    print(html)
