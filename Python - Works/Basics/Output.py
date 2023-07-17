# To Perform the Code, Enter the Numbers in the Command line by following the given words.    py Output.py
# Ex : py Output.py 1 2 3 4 5 

from sys import argv

# print (argv)

""" print(argv[1])
print (argv[2])
print (argv[3])
print (argv[4])
print (argv[5]) """

# for arg in argv:
#     print (arg)

# print ((argv[1])+(argv[2])+(argv[3])+(argv[4])+(argv[5]))                      # Concatination Process

# print (int(argv[1])+int(argv[2])+int(argv[3])+int(argv[4])+int(argv[5]))      # Addition Process


Concat = (argv[1])+(argv[2])+(argv[3])+(argv[4])+(argv[5])

Addition = int(argv[1])+int(argv[2])+int(argv[3])+int(argv[4])+int(argv[5])

print ("Addition of CMD Line Arguements : ", Addition)
print ("Concatination of CMD Line Arguements : ", Concat)