# WAP for Fibonacci Sequence

n = int(input('Enter the Number for Fibonacci Sequence : '))

a = 0
b = 1

for _ in range(n):    
    a, b = b, a + b
    print(a, end=' ')
