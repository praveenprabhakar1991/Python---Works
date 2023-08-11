# WAP for Diamond Pattern for Increasing Numbers

print('Diamond Pattern for Increasing Numbers')

col = 5
row = 1

for i in range(col-1):
    for j in range(i,col):
        print(' ', end = ' ')
    for j in range(i+1):
        print(row, end = ' ')
    for j in range(i):
        print(row, end = ' ')
    row += 1
    print()

for i in range(col):
    for j in range(i+1):
        print(' ', end = ' ')
    for j in range(i,col):
        print(row, end = ' ')
    for j in range(i,col-1):
        print(row, end = ' ')
    row -= 1
    print()
    
# WAP for Diamond Pattern for Increasing Odd Numbers

print('Diamond Pattern for Increasing Odd Numbers')

col = 5
row = 1

for i in range(col-1):
    for j in range(i,col):
        print(' ', end = ' ')
    for j in range(i+1):
        print(row, end = ' ')
    for j in range(i):
        print(row, end = ' ')
    row += 2
    print()
    
for i in range(col):
    for j in range(i+1):
        print(' ', end = ' ')
    for j in range(i,col):
        print(row, end = ' ')
    for j in range(i,col-1):
        print(row, end = ' ')
    row -= 2
    print()
    
# WAP for Diamond Pattern for Increasing Odd Numbers

print('Diamond Pattern for Increasing Odd Numbers')

col = 5
row = 0

for i in range(col-1):
    for j in range(i,col):
        print(' ', end = ' ')
    for j in range(i+1):
        print(row, end = ' ')
    for j in range(i):
        print(row, end = ' ')
    row += 2
    print()
    
for i in range(col):
    for j in range(i+1):
        print(' ', end = ' ')
    for j in range(i,col):
        print(row, end = ' ')
    for j in range(i,col-1):
        print(row, end = ' ')
    row -= 2
    print()