#implicit inheritance
class Parent(object):
    def implicit(self):
        print("PARENT implicit()")
class Child(Parent):#This class inherit the parent class
    pass
dad = Parent()
son = Child()
dad.implicit()
son.implicit() #Object of child class accessing the function inside parent class