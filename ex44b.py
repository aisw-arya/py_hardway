#override explicity
class Parent(object):
    def override(self):
        print("PARENT override()")
class Child(Parent):#This class inherit the parent class
    def override(self):
        print("CHILD override()")
dad = Parent()
son = Child()
dad.override()
son.override()