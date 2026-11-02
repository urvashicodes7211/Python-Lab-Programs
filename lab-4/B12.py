#WAP to print sum of digits of given number.

n = int(input("Enter n : "))

sum = 0

while n > 0:
    m = n % 10
    sum = sum + m
    n = n // 10

print(sum)
