#WAP to print given 3 numbers in descending order?

a = 654
b = 345
c = 987

num = a,b,c
print(sorted(num,reverse=True))

print ("***** You Can Try *****")

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))

num = a,b,c
print("Here is the Sequence of Descending Order : ", sorted(num,reverse=True))
