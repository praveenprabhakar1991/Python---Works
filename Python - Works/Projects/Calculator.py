# WAP for Calculator

"""
a = input("Enter First Number:")            # Concatination process won't go under calculation
b = input("Enter Second Number:") 
"""

print("***My Calculator***")

while True:  
    a = int(input("\nEnter First Number : "))
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
    
    user = input("\nEnter Q to Quit / Enter any key to Continue : ").lower()
    
    if user == 'q':
        break
    
    if user not in 'q':
        continue