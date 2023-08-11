# Print Reverse Right Angle Triangle Pattern with ‘*’ Symbol
''' * * * * *
    * * * *
    * * *
    * *
    * '''

for i in range(5):
    for j in range(i,5):
        print('*', end = ' ')
    print()

print('\n*** You Can Try ***\n')

user = int(input('Enter any Number : '))

for i in range(user):
    for j in range(i,user):
        print('*', end = ' ')
    print()