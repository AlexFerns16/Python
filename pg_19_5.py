# encapsulation

class Parent:
    def __init__(self):
        self.__name = 'John'
        self._age = 27
        self.prof = 'Banker'

    def display(self):
        print(self.__name, self._age, self.prof)

class Child(Parent):
    def display(self):
        print(self.__name, self._age, self.prof)

objp = Parent()
objc = Child()

# objp.display()
# objc.display()

print(objc.prof)
# print(objc.__name)
print(objc._age)

# print(objp.__name)
