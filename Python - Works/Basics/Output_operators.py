# To Perform the Code, Enter the Numbers in the Command line by following the given words.    py Output_operators.py
# Ex : py Output_operators.py 1 2 3 4 5 

from sys import argv

sum = 0
sub = 0
multi = 1

list = argv[1:3
            ]                                     #Slicing  Process

print(argv)
print (list)

print ("*******************************")

for value in list:
    n = int(value)                                  # Type casting Conversion of int
    sum = sum + n

print ("Addition of CMD Line Arguements : ", sum)

for value in list:
    n = int(value)                                  # Type casting Conversion of int
    sub = sub - n
    
print ("Substraction of CMD Line Arguements : ", sub)

for value in list:
    n = int(value)                                  # Type casting Conversion of int
    multi = multi * n

print("Multiplication of CMD Line Arguements : ", multi)