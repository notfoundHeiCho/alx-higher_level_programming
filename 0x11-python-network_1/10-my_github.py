#!/usr/bin/python3
"""Prints the GitHub id of a user."""
import sys
import requests


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    headers = {'Authorization': f'Bearer {password}'}
    res = requests.get("https://api.github.com/user", headers=headers)
    if (res.status_code >= 400):
        print("None")
        exit()
    print(res.json()["id"])
