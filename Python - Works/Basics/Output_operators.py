from sys import argv

sum = 0
sub = 0
multi = 1

list = argv[1:]                                     #Slicing  Process

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