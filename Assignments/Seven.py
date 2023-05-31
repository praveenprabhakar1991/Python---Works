# WAP to print the least/small number is given two numbers?

a = 49
b = 50

if a < b:
    print("Yes, the small number is : ", a)
else:
    print("No, it is not a least number ")

print ("***** You Can Try *****")

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

if a < b:
    print("Yes, the Least Number is : ", a)
elif a > b:
    print("Yes, the Least Number is : ", b)
else:
    print("Oops Sorry, Same Number not Accessed. Try Again...")
