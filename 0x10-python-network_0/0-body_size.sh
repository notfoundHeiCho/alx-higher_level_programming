#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.
curl -sw '%{size_download}\n' -o /dev/null "$1"
