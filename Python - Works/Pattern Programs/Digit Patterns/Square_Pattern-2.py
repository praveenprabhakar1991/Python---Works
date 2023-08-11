# WAP for Square Pattern for Increasing Numbers

print("\nSquare Pattern in Increasing numbers\n")

col = 5
row = 1

for i in range(col):
    for j in range(col):
        print(row, end = ' ')
    row += 1
    print()

# WAP for Square Pattern for Increasing Odd numbers

print("\nSquare Pattern in Increasing Odd numbers\n")

col = 5
row = 1

for i in range(col):
    for j in range(col):
        print(row, end = ' ')
    row += 2
    print()
    
print("**************\n")

print("\nSquare Pattern in Increasing even numbers\n")
    
# WAP for Square Pattern for Increasing even number

col = 5
row = 0

for i in range(col):
    for j in range(col):
        print(row, end = ' ')
    row += 2
    print()