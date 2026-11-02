#WAP to count numbers of vowels in given string.

s = input("Enter s : ")
c = 0
for i in s:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        c = c + 1

print(c)