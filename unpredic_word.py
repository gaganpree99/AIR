#!/usr/bin/env python
import re

def check(text):
    i=0
    lines =["today","yesterday","now","time","dollar","money","price","currency","temperature","stock"]
    print lines[0]
    remove = '|'.join(lines)
    regex = re.compile(r'\b('+remove+r')\b', flags=re.IGNORECASE)
    out = regex.sub("", text)
    
    print"yellllll"
    print out
    print text
    
    if re.search(r"\b" + re.escape(text) + r"\b", out):
        print "not predicatable word present"
        return 1
        
    else:
        print "predicatable word present"
        return 0
