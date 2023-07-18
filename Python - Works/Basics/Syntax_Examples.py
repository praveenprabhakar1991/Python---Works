#                                                              Syntax

#                                                             Variable

x = 0

#                                                         Condition Operator

# *****************************                                if block                                        *****************************

if 1 > 0 :                                                     # if
    print("True")                                              # True

# *****************************                                if else block                                   *****************************

if 0 > 1 :                                                     # if
    print("True")                                              # True
else :                                                         # else
    print ("False")                                            # False
    
# *****************************                                if else block                                   *****************************

if 1 < 0 :                                                     # if  
    print("True")                                              # True
elif 1 <= 0 :                                                  # elif
    print("Equal")                                             # Equal
else :                                                         # else
    print("False")                                             # False
    
# *****************************                                Ternary                                         *****************************

1 if 1 > 0 else 0
print ("True")

#                                                          Iterative Operator

# *****************************                                for Loop                                        *****************************

for a in range(11):
    print(a)

# *****************************                                While Loop                                      *****************************

i = 1                                                          # Initialization

while i <= 10:                                                 # Condition
    print(i)
    i = i + 1                                                  # Increment / Decrement
    
# *****************************                                 Functions                                      *****************************

def add(a,b):                                                  # Arguments
    
    sum = a + b
    print(sum)

add(20,30)                                            # Invoke the function with Arguments

# *****************************                              return Function                                   *****************************

def add(a,b):                                                  # Arguments
    
    return a + b                                               # return statement

sum = add (10,100)                                    # Invoke the function with Arguments
print(sum)

# *****************************                              lambda Function                                   *****************************

multi = lambda x , y : x * y                                   # Arguments : Expression
# x = multi(10, 20)
# print(x)
print(multi(10,20))                                            # Invoke with Arguments

# *****************************                                  Class                                         *****************************

class Employee:
    id = 101
    
    def emp(self):
        print("emp Method")

obj = Employee()
obj.emp()


# *****************************                              Inheritance Class                                 *****************************

class Parent:
    
    def m1(self):
        print("Parent Class - m1() Method")

class Child(Parent):
    
    def m2(self):
        print("Child Class - m2() Method")

Obj = Child()
Obj.m1()
Obj.m2()