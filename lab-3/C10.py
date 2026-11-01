# WAP to find the second largest number among three user input numbers. 

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if(a>=b and a>=c):
    l = a
elif(b>=a and b>=c):
    l = b
else:
    l = c

if(a == l):
    if(b >= c):
        print("second largest number : ",b)
    else:
        print("second largest number : ",c)
elif(b == l):
    if(a >= c):
        print("second largest number : ",a)
    else:
        print("second largest number : ",c)
else:
    if(a >= b):
        print("second largest number : ",a)
    else:
        print("second largest number : ",b)