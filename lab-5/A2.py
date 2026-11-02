#WAP to reverse the words in given string. 

s = input("Enter string : ")

words = s.split()

rev = words[::-1]

print(" ".join(rev))