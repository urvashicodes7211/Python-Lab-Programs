#WAP to find the largest element in a list. 

list = [1,2,9,4,5]

l = list[0]

for i in range(0,len(list)):
    if(list[i] >= l):
        l = list[i]

print(l)