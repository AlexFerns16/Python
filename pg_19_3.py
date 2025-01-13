# multiple inheritance

class Parent1:
    def __init__(self):
        self.name = 'John'

class Parent2:
    def __init__(self):
        self.age = 24

class Child(Parent1, Parent2):
    def __init__(self):
        self.prof = "Banker"
        Parent1.__init__(self)
        Parent2.__init__(self)

    def display(self):
        print(self.name, self.age, self.prof)

objc = Child()
objc.display()
