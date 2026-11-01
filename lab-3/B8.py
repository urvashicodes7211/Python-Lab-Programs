"""WAP to read marks of five subjects. Calculate percentage and print class 
accordingly. Fail below 35, Pass Class between 36 to 45, Second Class between 
46 to 60, First Class between 61 to 70, Distinction if more than 70. """

m1 = int(input("Enter m1(1-100) : "))
m2 = int(input("Enter m2(1-100) : "))
m3 = int(input("Enter m3(1-100) : "))
m4 = int(input("Enter m4(1-100) : "))
m5 = int(input("Enter m5(1-100) : "))

per = ((m1 + m2 + m3 + m4 + m5)/500)*100

if(per < 35):
    print("Fail Class")
elif(per <= 45):
    print("Pass Class")
elif(per <= 60):
    print("Second Class")
elif(per <= 70):
    print("First Class")
else:
    print("Distinction")