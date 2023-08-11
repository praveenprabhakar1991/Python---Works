# WAP for Left Triangle Pattern for Increasing Numbers

print('\nLeft Triangle Pattern Increasing Numbers\n')

col = 5
row = 1

for i in range(col):
    for j in range(i,col):
        print(' ', end = ' ')
    for j in range(i+1):
        print(row, end = ' ')
    row += 1
    print()

# WAP for Left Triangle Pattern for Increasing Odd Numbers

print('\nLeft Triangle Pattern Increasing Odd Numbers\n')

col = 5
row = 1

for i in range(col):
    for j in range(i,col):
        print(' ', end = ' ')
    for j in range(i+1):
        print(row, end = ' ')
    row += 2
    print()
    
# WAP for Left Triangle Pattern for Increasing Even Numbers

print('\nLeft Triangle Pattern Increasing Even Numbers\n')

col = 5
row = 0

for i in range(col):
    for j in range(i,col):
        print(' ', end = ' ')
    for j in range(i+1):
        print(row, end = ' ')
    row += 2
    print()