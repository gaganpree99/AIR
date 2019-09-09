#!/usr/bin/python

import wolframalpha
import sys
import remove
import os
import auto_offline_db_maker
import duplicate_remover
import re
import session_forall

# Get a free API key here http://products.wolframalpha.com/api/
# This is a fake ID, go and get your own, instructions on my blog.
app_id='KHE5G2-42E4UX5AL3'

client = wolframalpha.Client(app_id)

query = ' '.join(sys.argv[1:])
res = client.query(query)

if len(res.pods) > 0:
    texts = ""
    pod = res.pods[1]
    pod2 = res.pods[0]
    if pod.text:
        texts = pod.text
    elif pod2.text:
        texts= pod2.text		
    
    else:
        texts = "I have no answer for that"
    # to skip ascii character in case of error
    texts = texts.encode('ascii', 'ignore')
    a= texts.replace("Wolfram|Alpha", "AIR")
    b=a.replace("Noun | ", "")
    c=b.replace("noun | ", "")
    print c.replace("| noun | ", "")
    os.system("./s.sh '%s'" %(c))
    lcd=c.replace("\n", " , ")
    auto_offline_db_maker.save(lcd)
    q = open("stt1.txt","r").readlines()
    g=q[0].replace("\n","")
    print g
    save=duplicate_remover.check(g)
    if(save==1):
        session_forall.q(g)#to save every ask question
        session_forall.ans(lcd)
else:
    print "Sorry, I am not sure."
    os.system("./s.sh 'Sorry, I am not sure.'")

