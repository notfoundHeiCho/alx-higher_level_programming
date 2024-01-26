#!/usr/bin/python3
"""Sends a form data to a URL."""
import sys
import requests

if __name__ == '__main__':
    me = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(str(me.text))
