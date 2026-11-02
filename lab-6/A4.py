#WAP to interchange first and last elements in a list.

# WAP to interchange first and last elements in a list.

list = [1, 2, 3, 4, 5]

temp = list[0]
list[0] = list[-1]
list[-1] = temp

print(list)