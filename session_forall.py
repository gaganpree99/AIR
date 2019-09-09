
def q(question):
    
    f = open("session_forall_q.txt","a")
    if len(question)==0:
        exit()
    f.writelines("%s \n"%(question))        
    
def ans(answer):
    d = open("session_forall_ans.txt","a")
    if len(answer)==0:
        pass
    ans=answer.replace("\n", "")    
    d.writelines("%s \n"%(ans))