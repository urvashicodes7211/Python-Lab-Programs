#WAP to swap two numbers.

"""a = int(input("Enter a : "))
b = int(input("Enter b : "))

a = a + b
b = a - b
a = a - b

print(a)
print(b)"""

a = int(input("Enter a : "))
b = int(input("Enter b : "))

a,b = b,a

print(a)
print(b)