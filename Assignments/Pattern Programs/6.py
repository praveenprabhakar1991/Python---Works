# Print square pattern with given digit in descending order

''' 5 5 5 5 5
    4 4 4 4 4
    3 3 3 3 3
    2 2 2 2 2
    1 1 1 1 1 '''

col = 5
row = 5

for i in range(col):
    for j in range(col):
        print(row, end = ' ')
    row -= 1
    print()    