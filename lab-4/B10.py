#WAP to find whether the given number is prime or not. 

n = int(input("ENter n : "))

c = 0

for i in range(1,n+1):
    if(n % i == 0):
        c = c + 1

if(c == 2):
    print("prime")
else:
    print("Not prime")
    