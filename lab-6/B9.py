# WAP to count unique items in a list. 

list = [1,2,2,3,4,4,5]

unique = []

for i in list:
    if(i not in unique):
        unique.append(i)

print(len(unique))