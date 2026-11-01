"""Three sides of a triangle are entered through the keyboard, WAP to check 
whether the triangle is isosceles, equilateral, scalene or right-angled triangle. """

s1 = int(input("Enter s1 : "))
s2 = int(input("Enter s2 : "))
s3 = int(input("Enter s3 : "))

if(s1 <= 0 or s2 <= 0 or s3 <= 0):
    print("Invalid triangle")
elif(s1 + s2 <= s3 or s2 + s3 <= s1 or s3 + s1 <= s2):
    print("Invalid triangle")
elif(s1 == s2 and s2 == s3):
    print("equilateral triangle")
elif(s1*s1 + s2*s2 == s3*s3 or s2*s2 + s3*s3 == s1*s1 or s3*s3 + s1*s1 == s2*s2):
    print("right-angled triangle")
elif(s1 == s2 or s2 == s3 or s3 == s1):
    print("isosceles triangle")
else:
    print("scalene triangle")