#!/bin/bash
# Displays only the status code of the response.
curl "$1" | awk '/1.0/{print $2}'
