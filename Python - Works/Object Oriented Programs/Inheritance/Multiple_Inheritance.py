class Parent1:
    
    def m1(self):
        print("Parent1 Class - m1() Method")
    
    def m2(self):
        print("Parent1 Class - m2() Method")

class Parent2:
    
    def m1(self):
        print("Parent2 Class - m1() Method")
    
    def m2(self):
        print("Parent2 Class - m2() Method")

class Child(Parent1,Parent2):
    
    def m3(self):
        print("Child Class - m3() Method")

Obj = Child()
Obj.m1()
Obj.m2()
Obj.m3()