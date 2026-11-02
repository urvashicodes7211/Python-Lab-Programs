#WAP to find GCD of the given two numbers.

a = int(input("Enter a : "))
b = int(input("Enter b : "))

while(b != 0):
    m = a % b
    a = b
    b = m

print(a)