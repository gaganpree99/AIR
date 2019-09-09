import sys
import re
def pattern(word):
    f=[]
    print word

    i=0
    
    lines = open( "stt.txt", "r" ).readlines()

    for line in lines:
        i=i+1
        if re.search(r"\b" + re.escape(word) + r"\b", line):
	    f.append(i)
    return f 

def cmd_pattern(word):
    f=[]
    print word
    print "hhrhhr"

    i=0
    
    lines = open( "cmd_q.txt", "r" ).readlines()

    for line in lines:
        i=i+1
        if re.search(r"\b" + re.escape(word) + r"\b", line):
	    f.append(i)
    print f    
    return f 
    