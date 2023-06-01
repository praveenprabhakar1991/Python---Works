#WAP to calculate the sum of the first 10 natural numbers using for Loop and While loop?

list = [1,2,3,4,5,6,7,8,9,10]

sum = 0

for i in list:
    sum = sum + i
    
print("The Sum of the first 10 natural numbers using for Loop", sum)

sum = 0

i = 1
while i <= 10:
    sum = sum + i
    i = i + 1

print("The Sum of the first 10 natural numbers using While Loop", sum)