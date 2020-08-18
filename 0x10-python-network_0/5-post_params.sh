#!/bin/bash
# Sends a post request
curl -sX POST -d 'email=hr@holbertonschool.com&subject=I will always be here for PLD' "$1"
