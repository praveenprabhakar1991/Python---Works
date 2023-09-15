# WAP for Martingale Sequence [1,2,4,8,16,32,64,128,256,512,1024,...]

n = int(input('Enter the Number for Martingale Sequence : '))

a = 1
b = 5

sequence = []

for _ in range(n):
    sequence.append(a)
    a = a * b
    
print(sequence)