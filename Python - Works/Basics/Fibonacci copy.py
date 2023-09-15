# Prompt the user for the number of terms
n = int(input("Enter the number of terms for the Fibonacci sequence: "))

a = 0
b = 1

# Check if the input is valid
if n <= 0:
    print("Please enter a positive integer.")
    
elif n == 1:
    print("Fibonacci sequence:")
    print(a)
    
else:
    # Print the first two terms
    print("Fibonacci sequence:")
    print(a, b, end=" ")

    for _ in range(2, n):
        next_term = a + b
        print(next_term, end=" ")
        a, b = b, next_term

print()