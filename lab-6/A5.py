# WAP to split the list into two parts and append the first part to the end. 

# WAP to split the list into two parts and append the first part to the end.

l = [1,2,3,4,5,6]

n = len(l) // 2

first = l[:n]
second = l[n:]

res = second + first

print(res)