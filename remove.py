#!/usr/bin/python
import re

def remove(text):

    REMOVE_LIST = ['what','when','how','why','is','am','are','to']
    remove = '|'.join(REMOVE_LIST)
    regex = re.compile(r'\b('+remove+r')\b', flags=re.IGNORECASE)
    out = regex.sub("", text)
    return out

def wolframeremove(text):

    REMOVE_LIST = ['wolfram','alpha','wolf','wolframalpha']
    remove = '|'.join(REMOVE_LIST)
    regex = re.compile(r'\b('+remove+r')\b', flags=re.IGNORECASE)
    bout = regex.sub("", text)
    return bout
