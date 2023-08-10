# WAP for ROCK PAPER SCISSOR Game

"""
a = input("Enter First Number:")            # Concatination process won't go under calculation
b = input("Enter Second Number:") 
"""
print("***My Calculator***\n")

while True:  
    a = int(input("Enter First Number : "))
    operator = (input("Enter Operator : "))
    b = int(input("Enter Second Number : "))    
        
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