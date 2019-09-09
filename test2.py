import sys
import re


def check(word):
    f=[]
    i=0
    filename = sys.argv[0]

    lines = open( "session_q.txt", "r" ).readlines()

    for line in lines:
        i=i+1
        if re.search(r"\b" + re.escape(word) + r"\b", line):
	    f.append(i)
	   
    return f 
