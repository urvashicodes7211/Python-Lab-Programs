# WAP to interchange the elements on two positions entered by a user.

list = [1,2,3,4,5]

p1 = int(input("Enter first position : "))
p2 = int(input("Enter second position : "))

temp = list[p1]
list[p1] = list[p2]
list[p2] = temp

print(list)