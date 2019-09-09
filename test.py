import sys
import re

f=[]
word = sys.argv[0]
print word


def check(word):
    i=0
    filename = sys.argv[0]

    lines = open( "stt.txt", "r" ).readlines()

    for line in lines:
        i=i+1
        if re.search(r"\b" + re.escape(word) + r"\b", line):
	    f.append(i)
	   
    return f 

def offline_check(word):
    i=0
    filename = sys.argv[0]

    lines = open( "session_q.txt", "r" ).readlines()

    for line in lines:
        i=i+1
        if re.search(r"\b" + re.escape(word) + r"\b", line):
	    f.append(i)
	   
    return f 


def cmd_check(word):
    i=0
    filename = sys.argv[0]

    lines = open( "cmd_q.txt", "r" ).readlines()

    for line in lines:
        i=i+1
        if re.search(r"\b" + re.escape(word) + r"\b", line):
	    f.append(i)
	   
    return f 

