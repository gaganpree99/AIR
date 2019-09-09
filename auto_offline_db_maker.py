#!/usr/bin/env python

import sys
import unpredic_word
import re
import sys

def save(t):
    print t

    f = open("stt1.txt","r")
    f1 = open("session_q.txt", "a")
    v = open("stt1.txt","r").readlines()
    g=v[1]
    g=g.replace("\n","")
    
    d=unpredic_word.check(g)
    print "value of d"
    print d

    if len(g)==0:
        print"zero"
        exit()
     
    
    if(d==1):
        print"jjjjjjjjjjj"
        f1.write(g)
        f3 = open("session_ans.txt", "a")
        f3.writelines("%s \n"%(t))
    else:
        print"nothing save"    

