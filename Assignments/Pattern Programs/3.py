# Print square pattern with '*' symbols

''' * * * * * 
    * * * * * 
    * * * * *
    * * * * *
    * * * * * '''

for i in range(5):
    for j in range(5):
        print('*', end=' ')
    print()

print('\n*** You Can Try ***\n')

user = int(input('Enter any Number : '))

for i in range(user):
    for j in range(user):
        print('*', end = ' ')
    print()