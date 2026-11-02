#WAP to check whether the given number is palindrome or not.

n = int(input("Enter n : "))

ori = n

rev = 0

while n > 0:
    m = n % 10
    rev = (rev * 10) + m
    n = n // 10

if(ori == rev):
    print("palindrome")
else:
    print("Not palindrome")