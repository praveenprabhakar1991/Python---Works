# Print Right Angle Triangle pattern with '*' symbol

''' * 
    * * 
    * * *
    * * * *
    * * * * * '''

for i in range(5):
    for j in range(i+1):
        print('*', end=' ')
    print()
    
print('\n*** You Can Try ***\n')

user = int(input('Enter any Number : '))

for i in range(user):
    for j in range(i+1):
        print('*', end = ' ')
    print()