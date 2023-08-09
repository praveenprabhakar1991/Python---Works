num = input("Enter any Number : ")
print (f"The Multiplication of {num} is :")

try:
    for i in range (1,11):
        print (f"{int(num)} * {i} = {int(num) * i}")
        
except:
    print ("Invalid Input!!!")
    print ("Enter Numbers only")
