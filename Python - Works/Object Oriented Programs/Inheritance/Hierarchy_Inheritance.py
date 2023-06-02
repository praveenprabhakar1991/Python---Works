class Parent:
    
    def m1(self):
        print("Parent Class - m1() Method")
    
    def m2(self):
        print("Parent Class - m2() Method")
    
class Child1(Parent):
    
    def m3(self):
        print("Child1 Class - m3() Method")

class Child2(Parent):
    
    def m4(self):
        print("child2 Class - m4() Method")

Obj1 = Child1()
Obj1.m1()
Obj1.m2()
Obj1.m3()

Obj2 = Child2()
Obj2.m1()
Obj2.m2()
Obj2.m4()