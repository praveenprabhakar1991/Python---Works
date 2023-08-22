# WAP for Calculator

"""
a = input("Enter First Number:")            # Concatination process won't go under calculation
b = input("Enter Second Number:") 
"""

print("\n***CALCULATOR***\n")

a = int(input('Enter First Number : '))
Operator = input('Enter the Operators : ')
b = int(input('Enter Second Number : '))

def Calci(a,b):
    
    if Operator == '+':
        print(a+b)

    elif Operator == '-':
        print(a-b)

    elif Operator == '*':
        print(a*b)

    elif Operator == '/':
        print(a/b)

    elif Operator == '%':
        print(a%b)  

    else:
        print('Invalid Operator Input')
        print('Enter Valid Operator ( + , - , * , / , % )')

Calci(a,b)