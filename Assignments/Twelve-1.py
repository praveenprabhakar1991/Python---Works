#WAP to print max number in given 3 numbers ?

a = 987
b = 879
c = 789

if a > b and a > c:
    print (a, "is the Maximum Number")
elif b > c:
    print (b, "is the Maximum Number")
else:
    print (c, "is the Maximum Number")

print ("***** You Can Try *****")

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))

if a > b and a > c:
    print (a, "is the Maximum Number")
elif b > c:
    print (b, "is the Maximum Number")
else:
    print (c, "is the Maximum Number")