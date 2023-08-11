# WAP for Right Triangle Pattern Numbers

col = 5
row = 1

for i in range(5):
    for j in range(i+1):
        print(row, end = ' ')
    print()

print('\n*** You Can Try ***\n')

user = int(input('Enter any Number : '))

for i in range(user):
    for j in range(i+1):
        print(user, end = ' ')
    print()