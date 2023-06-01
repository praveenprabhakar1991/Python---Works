#WAP Factors of 24 using while loop. Example : Factors of 24 are (1,3,4,6,12,24)

i = 1

print("Factors of 24 are:")

while i <= 24:
    if 24 % i == 0:
        print(i)
    i = i + 1