# Print square pattern with given fixed digit in every row

''' 1 1 1 1 1 
    2 2 2 2 2 
    3 3 3 3 3
    4 4 4 4 4
    5 5 5 5 5 '''

col = 5
row = 1

for i in range(col):
    for j in range(col):
        print(row, end = ' ')
    row += 1
    print()