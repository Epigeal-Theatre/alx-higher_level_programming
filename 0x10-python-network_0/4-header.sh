#!/bin/bash
# this send a GET request to the URL using curl, and then display the body of the response
curl -sH "X-School-User-Id: 98" "$1"
