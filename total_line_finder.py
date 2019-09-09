#!/usr/bin/env python


def q():
    i=0
    question= open("session_forall_q.txt","r").readlines()

    for f in question:
        i=i+1
    return i    

def a():
    i=0
    question= open("session_forall_ans.txt","r").readlines()

    for f in question:
        i=i+1
    return i 