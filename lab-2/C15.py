"""WAP to get day, month and year from the user and print the date in the given 
format: 20-10-2024. """

d = int(input("Enter day : "))
m = int(input("Enter month : "))
y = int(input("Enter year : "))

print(f"{d:02d}-{m:02d}-{y}")