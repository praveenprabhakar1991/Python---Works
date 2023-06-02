class GrandParent:
    
    def m1(self):
        print("GrandParent Class - m1() Method")
    
    def m2(self):
        print("GrandParent Class - m2() Method")

class Parent(GrandParent):
    
    def m3(self):
        print("Parent Class - m3() Method")
    
    def m4(self):
        print("Parent Class - m4() Method")

class Child(Parent):
    
    def m5(self):
        print("Child Class - m5() Method")

Obj = Child()
Obj.m1()
Obj.m2()
Obj.m3()
Obj.m4()
Obj.m5()