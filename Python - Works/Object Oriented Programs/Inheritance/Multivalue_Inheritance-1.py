class GrandParent:
    pass

class Parent(GrandParent):
    pass

class Child(Parent):
    pass

Obj = Child()