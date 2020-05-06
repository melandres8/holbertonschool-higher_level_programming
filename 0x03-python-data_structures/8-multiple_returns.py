#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        tup = (0, None)
    else:
        le = len(sentence)
        f = sentence[0]
        tup = (le, f)
    return tup
