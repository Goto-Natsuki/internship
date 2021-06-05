
import math
import numpy  as np

def search3(num):
    #primary_list=np.empty(0)
    #primary_list=np.zeros(num)
    primary_list=np.zeros(num, dtype=np.int)
    divide=np.arange(2, int(math.sqrt(num)+1)+1)
    i=0
    
    while num!=1:

        while num% divide[0] ==0:
            #primary_list.append( divide[0] )
            primary_list[i]=divide[0]
            #primary_list=np.append(primary_list,divide[0])
            num=num//divide[0]
            i+=1
        
        divide=divide[ divide % divide[0] !=0]
        
        if len(divide)==0:
            #primary_list.append( num )
            #primary_list=np.append(primary_list,num)
            primary_list[i]=num
            break
    
    primary_list=primary_list[primary_list!=0]
    return primary_list
