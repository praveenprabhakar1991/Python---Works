# Print square pattern with 'A' symbols

''' A A A A A 
    A A A A A 
    A A A A A
    A A A A A 
    A A A A A '''

for i in range(5):
    for j in range(5):
        print('A', end = ' ')
    print()

print('\n*** You Can Try ***\n')

user = int(input('Enter any Number : '))

for i in range(user):
    for j in range(user):
        print('A', end = ' ')
    print()