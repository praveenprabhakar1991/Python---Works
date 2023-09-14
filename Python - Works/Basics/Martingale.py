# WAP for Martingale Sequence [1,2,4,8,16,32,64,128,256,512,1024,...]

a = 1
b = 2

sequence = []

for _ in range(10):
    sequence.append(a)
    a = a * b
    
print(sequence)