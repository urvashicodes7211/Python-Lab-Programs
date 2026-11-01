"""WAP to calculate electricity bill based on following criteria. Which takes the 
unit from the user. 
i. First 1 to 50 units - Rs. 2.60/unit  
ii. Next 50 to 100 units - Rs. 3.25/unit 
iii. Next 100 to 200 units - Rs. 5.26/unita 
iv. bove 200 units - Rs. 8.45/unit """

u = int(input("Enter unit : "))

if(u <= 50):
    bill = u * 2.60
elif(u <= 100):
    bill = 50 * 2.60 + (u - 50) * 3.25
elif(u <= 200):
    bill = 50 * 2.60 + 50 * 3.25 + (u - 100) * 5.26
else:
    bill = 50 * 2.60 + 50 * 3.25 + (100) * 5.26 + (u - 200) * 8.45

print(bill)