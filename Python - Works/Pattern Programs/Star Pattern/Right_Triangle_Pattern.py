# WAP for Right Triangle Pattern

n = 5

for i in range(n):
    for j in range(i+1):
        print('*', end = ' ')
    print()

print('\n*** You Can Try ***')

user = int(input('Enter the Number : '))

for i in range(user):
    for j in range(i+1):
        print('*', end = ' ')
    print()