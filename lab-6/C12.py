# WAP to count occurrences of an element in a list. 

list = [1, 2, 3, 2, 4, 2, 5]

n = int(input("Enter element : "))

c = 0

for i in range(0, len(list)):
    if(list[i] == n):
        c = c + 1

print("occurrences :", c)