# WAP to find tuples with all positive elements from the given list of tuples.

list1 = [(1,2,3), (-1,2,3), (4,5,6), (2,-3,4)]

for i in list1:
    if(all(j > 0 for j in i)):
        print(i)