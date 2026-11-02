#WAP to print sum of series 1 – 2 + 3 – 4 + 5 – 6 + 7 ... n. 

n = int(input("Enter n : "))

sum = 0

for i in range(1,n+1):
    if(i % 2 == 0):
        sum = sum - i
    else:
        sum = sum + i

print(sum)