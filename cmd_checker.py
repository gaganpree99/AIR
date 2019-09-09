import test
import os 
import sys
import remove
import pattern
import search
import decimal

def cmd_checker(squery,fquery):
    collect=[]
    position=1;
    a=[]
    empty_list=[]
    print squery
    print fquery


    for i in range(len(squery)):
        
        f=test.cmd_check(squery[i])
        print f
        
    empty_list.append(f)

        
    print "empty : %s" %(empty_list)
    empty_list=sum(empty_list,[])
    print "new_empty : %s" %(empty_list)

       
    if not empty_list:
        return 0
        exit() 

    for s in range(len(empty_list)):
        b=empty_list.count(empty_list[s])
        
        a.append(b)    

    l= len(a)
    print squery
    
    fl= float(len(squery))
    ad = decimal.Decimal(fl/3)
    print(round(ad,0))
    print a
    try:   
        found=max(a)
        print found
        print "MAX FOUND"

    except:
        print "error"
        return 0
        sys.exit()
    else:    
        if (found<(len(squery)/2)+ad):
            return 0
            exit()
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
                    print "here"
                else:
                    try:
                        print "Pattern Intiating"
                        print fquery
                        pno=pattern.cmd_pattern(fquery)	
                       
                    
                    except:
                        print "Sorry "
                        return 0
                        
                    else:    
                        if (len(pno)==1):
                            print "Pattern Searching"
                            
                            search.cmd_search(pno[0],fquery) 
                            
                            sys.exit()   
                        
                        true=0
                    
                        break

                
                
        if(true==1):
            print "i am here"
            print empty_list[collect[0]]
            search.cmd_search(empty_list[collect[0]],fquery)
            return 1
        else:
            exit()
        


