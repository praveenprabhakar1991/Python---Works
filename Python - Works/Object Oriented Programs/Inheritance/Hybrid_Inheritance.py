class GrandParent1:
    pass

class GrandParent2:
    pass

class Parent(GrandParent1,GrandParent2):
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass

Obj = Child1()

Obj = Child2()