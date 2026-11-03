# WAP to remove tuples of length K. 

t = [(1,2), (3,4,5), (6,7), (8,9,10,11), (12,)]

k = int(input("Enter K : "))

res = []

for i in t:
    if(len(i) != k):
        res = res + [i]

print(res)