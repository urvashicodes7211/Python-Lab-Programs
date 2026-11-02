#WAP to capitalize the first and last character of each word in a string. 

s = input("Enter s : ")

words = s.split()

res = ""

for word in words:
    word = word[0].upper() + word[1:-1] + word[-1].upper()
    res = res + word + " "

print(res)