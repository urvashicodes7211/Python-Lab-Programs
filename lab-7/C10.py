#  WAP to test if the given tuple is distinct or not. 

t = (1,2,3,4,5)

if(len(t) == len(set(t))):
    print("Tuple is Distinct")
else:
    print("Tuple is Not Distinct")