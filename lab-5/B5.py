#WAP to print even length word in string. 

s = input("Enter s : ")

words = s.split()

for word in words:
    if(len(word) % 2 == 0):
        print(word)