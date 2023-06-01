#WAP to print min numbers in given 3 numbers using Ternary Operator?

a = 897
b = 789
c = 987

min = a if a < b and a < c else b if b < c else c
print("Yes, here is the minimum number : ",min)

print ("***** You Can Try *****")

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))

min = a if a < b and a < c else b if b < c else c
print("Yes, here is the minimum number : ",min)