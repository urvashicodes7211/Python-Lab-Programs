list = [1,1,2,3,2,4,2,1,4,3,5]

k = int(input("Enter K : "))
res = []
for i in list:
    if(list.count(i) > k):
        if(i not in res):
            print(i)
            res = res + [i]