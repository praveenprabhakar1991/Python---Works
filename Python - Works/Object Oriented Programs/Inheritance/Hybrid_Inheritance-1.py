class GrandParent1:
    
    def m1(self):
        print("GrandParent1 Class - m1() Method")

class GrandParent2:
    def m2(self):
        print("GrandParent2 Class - m2() Method")

class Parent(GrandParent1,GrandParent2):
    def m3(self):
        print("Parent Class - m3() Method")

class Child1(Parent):
    def m4(self):
        print("Child1 Class - m4() Method")

class Child2(Parent):
    def m5(self):
        print("Child2 Class - m5() Method")

Obj1 = Child1()
Obj1.m1()
Obj1.m2()
Obj1.m3()
Obj1.m4()

Obj2 = Child2()
Obj2.m1()
Obj2.m2()
Obj2.m3()
Obj2.m5()
