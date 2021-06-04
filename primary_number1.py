
def search(num):
    primary_list=[]
    i=2
    
    while num!=1:
        if num % i == 0:
            primary_list.append(i)
            num=num//i
        else:
            i+=1
    
    print(primary_list)
#search(100)
