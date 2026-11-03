# WAP to find second largest number in a list. 

list = [1,2,3,4,5]

l = list[0]
sl = list[0]

for i in range(0,len(list)):
    if(list[i] > l):
        sl = l
        l = list[i]
    elif(list[i] > sl and list[i] != l):
        sl = list[i]

print(sl)