class Parent1:
    
    def m1(self):
        print("Parent1 Class - m1()")
    
    def m2(self):
        print("Parent1 Class - m2()")

class Parent2:
    
    def m1(self):
        print("Parent2 Class - m1()")
    
    def m2(self):
        print("Parent2 Class - m2()")

class Child(Parent2,Parent1):
    
    def m3(self):
        print("Child Class - m3()")

Obj = Child()
Obj.m1()
Obj.m2()
Obj.m3()