# WAP for Right Triangle Pattern for Increasing Numbers

print('\nRight Triangle Pattern in Increasing Numbers\n')

col = 5
row = 1

for i in range(col):
    for j in range(i+1):
        print(row, end = ' ')
    row += 1
    print()

# WAP for Right Triangle Pattern for Increasing Odd Numbers

print('\nRight Triangle Pattern in Increasing Odd Numbers\n')

col = 5
row = 1

for i in range(col):
    for j in range(i+1):
        print(row, end = ' ')
    row += 2
    print()

# WAP for Right Triangle Pattern for Increasing Even Numbers

print('\nRight Triangle Pattern in Increasing Even Numbers\n')

col = 5
row = 0

for i in range(col):
    for j in range(i+1):
        print(row, end = ' ')
    row += 2
    print()

