#!/bin/bash
# script takes a URL, sends a request to that URL, and then displays size of the body of the response in bytes
curl -s $1 | wc -c
