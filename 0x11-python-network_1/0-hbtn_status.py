#!/usr/bin/python3
'''Python script that fetches https://intranet.hbtn.io/status'''
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()

print("Body response:")
print('    - type: ', type(html))
print('    - content: ', html)
print('    - utf8 content: ', html.decode('utf-8'))
