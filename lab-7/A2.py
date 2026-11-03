# WAP to find Maximum and Minimum K elements in a given tuple. 

t = (10,20,5,40,15,30)

k = int(input("Enter K : "))

t1 = sorted(t)

print("Minimum K elements : ", t1[:k])
print("Maximum K elements : ", t1[-k:])