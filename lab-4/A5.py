# WAP to print sum of 1 to n numbers. 

n = int(input("Enter n : "))

sum = 0

for i in range(1,n+1):
    sum = sum + i

print(sum)