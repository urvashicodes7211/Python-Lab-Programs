#WAP to find out largest number from given three numbers. 

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if(a>=b and a>=c):
    print("largest number : ",a)
elif(b>=a and b>=c):
    print("largest number : ",b)
else:
    print("largest number : ",c)