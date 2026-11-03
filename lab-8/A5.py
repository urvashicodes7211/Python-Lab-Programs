# WAP to check if two lists have at-least one element common.
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 3, 8, 9]

flag = 0

for i in list1:
    if(i in list2):
        flag = 1
        break

if(flag == 1):
    print("Lists have at least one common element.")
else:
    print("Lists have no common elements.")