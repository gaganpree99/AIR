#!/usr/bin/env python
import sys
import os

def cmd(n):
    print n
    if (n=="500"):#repeat previous question
        print "hi"
        os.system("python 500.py")
    elif (n=="501"): #repeat privious answer
       os.system("python 501.py")
    elif (n==502): #databse update
       os.system("")    
    elif (n==503): #da
       os.system("") 
    
    else:
        print"nothinf found"   
    