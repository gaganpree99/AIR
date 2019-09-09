#!/usr/bin/env python
import total_line_finder
import re


def check(q):
    s=total_line_finder.q()
    f=open("session_forall_q.txt", "r" ).readlines()
    d= "%s" % (f[s-1])
    d=d.replace("\n","")
    #print q
    #print d
    #print q
    if re.search(r"\b" + re.escape(q) + r"\b", d):
        print "Duplicate found"
        return 0
        
    else:
        print "NO Duplicate found"
        return 1
        

    