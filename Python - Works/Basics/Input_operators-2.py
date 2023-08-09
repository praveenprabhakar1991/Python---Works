"""
a = input("Enter First Number:")            # Concatination process won't go under calculation
b = input("Enter Second Number:") 
"""

a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))

sum = a + b                                                   # Addition
print (f"The value of {a} + {b} is   : {sum}")

sub = a - b                                                   # Subtraction
print (f"The value of {a} - {b} is   : {sub}")

multi = a * b                                                 # Multiplication
print (f"The value of {a} * {b} is   : {multi}")

expo = a ** b                                                 # Exponentiation
print (f"The value of {a} ** {b} is  : {expo}")

mod = a % b                                                   # Modulus
print (f"The value of {a} % {b} is   : {mod}")

div = a / b                                                   # Division
print (f"The value of {a} / {b} is   : {div}")

floor_div = a // b                                            # Floor division
print (f"The value of {a} // {b} is  : {floor_div}")