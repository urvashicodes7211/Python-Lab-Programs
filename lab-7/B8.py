# WAP to remove duplicates from tuple. 

t = (1,2,3,2,4,1,5)

t1 = ()

for i in t:
    if(i not in t1):
        t1 = t1 + (i,)

print(t1)