# WAP to print the greatest number in given two numbers?

a = 2500
b = 2499

if a > b:
    print("Yes, greatest number is : ", a)
else:
    print("No, it is not a greatest number ")
    
print ("***** You Can Try *****")

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

if a > b:
    print("Yes, the greatest number is : ", a)
elif a < b:
    print("Yes, the greatest number is : ", b)
else:
    print("Oops Sorry, Same Number not Accessed. Try Again...")