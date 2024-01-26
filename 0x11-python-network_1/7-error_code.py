#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    if (res.status_code >= 400):
        print(f"Error code: {res.status_code}")
        exit()
    print(res.text)
