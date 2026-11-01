"""WAP to implement simple calculator which performs (addition, subtraction, 
multiplication and division) of two numbers based on user input. """

a = int(input("Enter a : "))
b = int(input("Enter b : "))

c = int(input("Enter a number : 1 : addition, 2 : subtraction, 3 : multiplication, 4 : division : "))

if(c == 1):
    result = a + b
    print("Addition : ",result)
elif(c == 2):
    result = a - b
    print("Subtraction : ",result)
elif(c == 3):
    result = a * b
    print("Multiplication : ",result)
elif(c == 4):
    result = a / b
    print("Division : ",result)
else:
    print("invalid number!!")