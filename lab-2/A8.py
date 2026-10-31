#WAP to convert degree into Fahrenheit and vice versa.

c = float(input("Enter Celsius : "))
f = (c*1.8)+32
print(f)

f = float(input("Enter Fahrenheit : "))
c = (f - 32) / 1.8
print("Celsius : ", c)