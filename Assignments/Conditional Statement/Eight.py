#WAP to print the greatest number in given three numbers?

a = 456
b = 879
c = 789

if a > b and a > c:
    print (a, "is the Greatest Number in given three number")
elif b > c:
    print (b, "is the Greatest Number in given three number")
else:
    print (c, "is the Greatest Number in given three number")

print ("***** You Can Try *****")

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))

if a > b and a > c:
    print (a, "is the Greatest Number in given three number")
elif b > c:
    print (b, "is the Greatest Number in given three number")
else:
    print (c, "is the Greatest Number in given three number")