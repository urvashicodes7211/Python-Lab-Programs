"""WAP to get the distance from user into kilometer, and convert it into meter, 
feet, inches and centimeter."""

k = float(input("Enter k : "))

m = k * 1000
f = k * 3280.84
i = k * 39370.1
c = k * 100000

print("Meter : ",m)
print("Feet : ",f)
print("Inches : ",i)
print("Centimeter : ",c)