#WAP to remove ith character from given string. 

s = input("Enter string : ")
i = int(input("Enter i : "))

s = s[:i] + s[i+1:]

print(s)