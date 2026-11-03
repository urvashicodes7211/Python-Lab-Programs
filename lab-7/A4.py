"""WAP to create a list of tuples from given list having number and its cube in 
each tuple. """

list1 = [1,2,3,4,5]

list2 = []

for i in list1:
    list2 = list2 + [(i, i**3)]

print(list2)