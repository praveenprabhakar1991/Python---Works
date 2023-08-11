# Print square pattern with given number/digit 

''' 5 5 5 5 5 
    5 5 5 5 5 
    5 5 5 5 5
    5 5 5 5 5
    5 5 5 5 5 '''

for i in range(5):
    for j in range(5):
        print('5', end = ' ')
    print()
    
print('\n*** You Can Try ***\n')

user = int(input('Enter any Number : '))

for i in range(user):
    for j in range(user):
        print('5', end = ' ')
    print()