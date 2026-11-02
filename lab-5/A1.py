#WAP to check given string is palindrome or not.

s = input("Enter string : ")

rev = s[::-1]

if(rev == s):
    print("palindrome")
else:
    print("Not palindrome")