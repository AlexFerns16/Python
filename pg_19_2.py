# multilevel inheritance

class Parent:
    def __init__(self):
        self.name = 'Thomas'

class Child(Parent):
    def __init__(self):
        self.age = 25
        Parent.__init__(self)

class GChild(Child):
    def __init__(self):
        print(self)
        self.prof = 'Banker'
        Child.__init__(self)

    def display(self):
        print(self)
        print(self.name, self.age, self.prof)

objgc = GChild()
objgc.display()
