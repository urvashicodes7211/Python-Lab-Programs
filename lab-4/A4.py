"""WAP to print numbers between two given numbers which is divisible by 2 but 
not divisible by 3."""

a = int(input("Enter a : "))
b = int(input("Enter b : "))

for i in range(a,b+1):
    if(i % 2 == 0 and i % 3 != 0):
        print(i)