#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status'''
import requests


html = requests.get('https://intranet.hbtn.io/status').text

print("Body response:")
print('\t- type:', type(html))
print('\t- content:', html)
