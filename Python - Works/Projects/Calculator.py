"""
a = input("Enter First Number:")            # Concatination process won't go under calculation
b = input("Enter Second Number:") 
"""
print("***Calculator***")

a = int(input("Enter First Number:"))
operator = (input("Enter Operator:"))
b = int(input("Enter Second Number:"))

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
elif operator == "%":
    print(a % b)
else:
    print("Warning! Invalid Operator Input.")
    print("Input the Valid Operators like ( + , - , * , / , %).")