#!/usr/bin/python3
'''Python script that sends a request to the URL'''
import requests
import sys


if __name__ == "__main__":
    res = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2],
        sys.argv[1])
    )
    if res.status_code >= 400:
        print('None')
    else:
        for comment in res.json()[:10]:
            print("{}: {}".format(
                comment.get('sha'),
                comment.get('commit').get('author').get('name'))
            )
