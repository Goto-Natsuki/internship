
import math

def search2(num):
    primary_list=[]
    divide=[i for i in range(2,int(math.sqrt(num)+1)+1)]
    
    while num!=1:

        while num% divide[0]==0:
            primary_list.append( divide[0] )
            num=num//divide[0]
        
        divide_copy=[j for j in divide if j % divide[0] !=0]
        divide=divide_copy[:]
        
        if len(divide)==0:
            primary_list.append( num )
            break
    
    return primary_list
