#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status'''
import requests


with requests.get('https://intranet.hbtn.io/status') as response:
    html = response.text

print("Body response:")
print('\t- type:', type(html))
print('\t- content:', html)
