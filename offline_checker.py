import sys
import test
import search
import os
import test2
import remove




def query(mquery):
    print "enter succesful"
    collect1=[]
    position1=1;
    a1=[]
    empty_list1=[]
    print mquery
    dquery=mquery.split()


    if (len(dquery)<2):
        fquery=mquery
        
    else:
        fquery=mquery

    fquery=remove.remove(fquery)
    squery=fquery.split()
    for i in range(len(squery)):
        f1=test2.check(squery[i])
        print f1
        empty_list1.append(f1)
    empty_list1=sum(empty_list1,[])
    print "empty : %s" %(empty_list1)

       
    if not empty_list1:
        print "Wait... search in the internet"       
        os.system("python qw.py '%s'" %(fquery))
        sys.exit() 

    for s in range(len(empty_list1)):
        b=empty_list1.count(empty_list1[s])
        
        a1.append(b)    

    l= len(a1)

    print a1
    try:   
        found=max(a1)
    except:
        print "error"
        sys.exit()
    else:        
        if (found<len(squery)):
            print "i am here"
            print "Wait... search in the internet"
            #offline_checker.query(squery) 
            os.system("python qw.py '%s'" %(fquery))
            sys.exit()
    for position1, item in enumerate(a1):
        if item == found:
            collect1.append(position1)
            



    true=1
    for i in range(len(collect1)):
        if(true==1):
            if empty_list1[collect1[i-1]]==empty_list1[collect1[i]]:
                true=1
            else:	
                pno=pattern.pattern(fquery)	
                print pno[0]
                if (len(pno)==1):
                    search.search(pno[0],mquery) 
                    sys.exit()   
                
                true=0
                
                breaks

            
            
    if(true==1):
        print empty_list1[collect1[0]]
        search.offline_search(empty_list1[collect1[0]],mquery)
    else:
        print "Wait... search in the internet"
        #offline_checker.query(squery) 
        os.system("python qw.py '%s'" %(fquery))
        sys.exit()

    
    

