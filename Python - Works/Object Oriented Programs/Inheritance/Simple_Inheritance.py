class Parent:
    
    def m1(self):
        print("Parent Class - m1() Method")
    
    def m2(self):
        print("Parent Class - m2() Method")

class Child(Parent):
    
    def m3(self):
        print("Child Class - m3() Method")

Obj = Child()
Obj.m1()
Obj.m2()
Obj.m3()
