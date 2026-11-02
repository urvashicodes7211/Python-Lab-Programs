#  WAP to print all odd numbers in a given range.

a = int(input("enter a : "))
b = int(input("Enter b : "))

for i in range(a,b+1):
    if(i % 2 != 0):
        print(i)