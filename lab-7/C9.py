# WAP to multiply adjacent elements of a tuple.

t = (1, 2, 3, 4, 5)

res = ()

for i in range(0, len(t)-1):
    mul = t[i] * t[i+1]
    res = res + (mul,)

print(res)