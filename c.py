import test
import search
import os 
import sys
import remove
import offline_checker
import time
import pattern
import cmd_checker
import decimal


collect=[]
position=1;
a=[]
empty_list=[]
mquery=sys.argv[1]
mquery=mquery.replace("'s"," is")
mquery=mquery.replace("'re"," your")
mquery=mquery.replace("'ve"," have")



print"You ask ... %s" %(mquery)
#os.system("./s.sh 'you ask to me...%s'" %(mquery)),

#mquery=remove.remove(query) 
dquery=mquery.split()

cmd_find=cmd_checker.cmd_checker(dquery,mquery)
#print "value of cmd_find:'%s' "%(cmd_find)

print "yoyoyoyo"

if (cmd_find==0):

    if (len(dquery)<2):
        fquery=mquery
        
    else:
        fquery=mquery


    squery=fquery.split()




    for i in range(len(squery)):
        
        f=test.check(squery[i])
        print f
        
    empty_list.append(f)

        
    print "empty : %s" %(empty_list)
    empty_list=sum(empty_list,[])
    print "new_empty : %s" %(empty_list)

       
    if not empty_list:
        print "Wait... check into database"
        offline_checker.query(mquery)        
        #os.system("python qw.py '%s'" %(fquery))
        sys.exit() 

    for s in range(len(empty_list)):
        b=empty_list.count(empty_list[s])
        
        a.append(b)    

    l= len(a)
    print squery
    #k=5/2
    #print "k:%s"%(k)
    #print len(((squery)/2))

    print a
    print "lenenene"
    fl= float(len(squery))
    ad = decimal.Decimal(fl/3)
    print(round(ad,0))

    print len(squery)/3
    try:   
        found=max(a)
        print "found next"
        print found
        

    except:
        print "error fgfg "
        sys.exit()
    else:    
        if (found<(len(squery)/2)+ad):
            print "Wait... check into database"
            offline_checker.query(mquery) 
            #ans=os.system("python qw.py '%s'" %(fquery))
            
            sys.exit()
        for position, item in enumerate(a):
            print "i am in"
            if item == found:
                collect.append(position)
            print collect    
                



        true=1
        for i in range(len(collect)):
            print "yippi"
            if(true==1):
                if empty_list[collect[i-1]]==empty_list[collect[i]]:
                    true=1
                else:
                    try:
                        pno=pattern.pattern(fquery)	
                        print pno[0]
                    
                    except:
                        print "Sorry "
                        
                    else:    
                        if (len(pno)==1):
                            search.search(pno[0],mquery) 
                            sys.exit()   
                        
                        true=0
                    
                        break

                
                
        if(true==1):
            print empty_list[collect[0]]
            search.search(empty_list[collect[0]],mquery)
        else:
            print "Wait... check into database"
            offline_checker.query(mquery) 
            sys.exit()
        



        
    #search.search(f)
else:
    exit()
    


