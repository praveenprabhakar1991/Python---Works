# WAP for Left Pascal Triangle Pattern

col = 5

for i in range(col-1):
    for j in range(i+1):
        print('*', end = ' ')
    print()

for i in range(col):
    for j in range(i,col):
        print('*', end = ' ')
    print()