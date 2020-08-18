#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept.
curl "$1" | awk '/Allow/' | cut -d " " -f2-
