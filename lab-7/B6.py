# WAP to add tuple to list and vice-versa.

l = [1,2,3,4,5]
t = (6,7,8,9,10)

l = l + list(t)
print("List :",l)

t = t + tuple(l)
print("Tuple :",t)