import sys
import os
import cmd_int
import session_forall
import duplicate_remover

def search(i,q):
    lines = open("result.txt", "r" ).readlines()

    s= "%s" % (lines[i-1] )
    save=duplicate_remover.check(q)
    if(save==1):
        session_forall.q(q)#to save every ask question
        session_forall.ans(s)
    print s
    os.system("./s.sh '%s'" %(lines[i-1] ))
        

def offline_search(i,q):
    lines = open("session_ans.txt", "r" ).readlines()

    s= "%s" % (lines[i-1] )
    s=s.replace("\n","")
    save=duplicate_remover.check(q)
    print s
    if(save==1):
        session_forall.q(q)#to save every ask question
        session_forall.ans(s)
    os.system("./s.sh '%s'" %(lines[i-1] ))

def cmd_search(i,q):
    lines = open("cmd_ans.txt", "r" ).readlines()
    s= "%s" % (lines[i-1] )
    d=s.replace("\n", "")
    print "%s" %d
    print"heheheheh"
    #session_forall.q(qs)#to save every ask question
    #session_forall.ans(d)
    if (d.isdigit()):
        print "xolo"
        cmd_int.cmd(d)
        
    else:    
        os.system("./s.sh '%s'" %(lines[i-1] ))
       
def every_q(i):
    lines = open("session_forall_q.txt", "r" ).readlines()

    s= "%s" % (lines[i-1] )
    print s
    os.system("./s.sh 'you ask to me...%s'" %(lines[i-1] ))
    

def every_ans(i):
    lines = open("session_forall_ans.txt", "r" ).readlines()

    s= "%s" % (lines[i-1] )
    print s
    os.system("./s.sh 'your answer of last question is %s'" %(lines[i-1] ))    