"""WAP to find out largest number from given two numbers using simple if and 
ternary operator. """

"""a = int(input("Enter a : "))
b = int(input("Enter b : "))

if(a > b):
    print("largest number : ",a)
else:
    print("largest number : ",b)"""

a = int(input("Enter a : "))
b = int(input("Enter b : "))

largest = a if a > b else b

print("largest number : ",largest)
