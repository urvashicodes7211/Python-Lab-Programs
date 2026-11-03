# WAP to find tuples which have all elements divisible by K from a list of tuples.

t = [(2,4,6), (3,5,7), (4,8,12), (5,10,15)]

k = int(input("Enter K : "))

for i in t:
    c = 0
    for j in i:
        if(j % k == 0):
            c = c + 1
    if(c == len(i)):
        print(i)