# inheritance ----------------------------------

# code 1 ---------------------------

# class Parent:
#     print('Hello_Parent')
#     def __init__(self, n):
#         self.name = n

# class Child(Parent):
#     print('Hello_Child')
#     def display(self):
#         print(self.name)

# objc = Child('John')
# objc.display()


# code 2 ---------------------------

class Parent:
    def __init__(self):
        print(self)
        self.name = 'Thomas'

class Child(Parent):
    def __init__(self, a):
        self.age = a
        print(self)
        super().__init__()

    def display(self):
        print(self.name, self.age)

objc = Child(27)
objc.display()


# code 3 ---------------------------

# class Parent:
#     def __init__(self):
#         self.name = input('Enter the Name: ')

# class Child(Parent):
#     def __init__(self, a):
#         self.age = a
#         super().__init__()

#     def display(self):
#         print(self.name, self.age)

# objc = Child(27)
# objc.display()


# code 4 ---------------------------

# class Parent:
#     def __init__(self, n):
#         self.name = n

# class Child(Parent):
#     def __init__(self, a, n):
#         self.age = a
#         super().__init__(n)
#         # Parent.__init__(self, n)

#     def display(self):
#         print(self.name, self.age)

# objc = Child(27, 'Thomas')
# objc.display()


# code 5 ---------------------------

# class Parent:
#     def __init__(self, n):
#         self.name = n

#     def display(self):
#         print(self.name)

# class Child(Parent):
#     def __init__(self, a, n):
#         self.age = a
#         super().__init__(n)

#     def display(self):
#         print(self.name, self.age)

# objp = Parent('Thomas')
# objp.display()

# objc = Child(27, 'John')
# objc.display()

# print(objp.name)
# print(objc.name)


# code 6 ---------------------------

# class Parent:
#     def __init__(self, n):
#         self.name = n

# class Child(Parent):
#     def __init__(self, a):
#         self.age = a
#         super().__init__(objp.name)

#     def display(self):
#         print(self.name, self.age)

# objp = Parent('Thomas')
# objc = Child(27)
# objc.display()


# code 7 ---------------------------

# class Parent1:
#     def __init__(self, n):
#         self.name_one = n

# objp1 = Parent1('Thomas')


# class Parent2:
#     def __init__(self, n):
#         self.name_two = n

# objp2 = Parent2('John')


# class Child(Parent1, Parent2):
#     def __init__(self, a):
#         self.age = a
#         Parent1.__init__(self, objp1.name_one)
#         Parent2.__init__(self, objp2.name_two)

#     def display(self):
#         print(self.name_one, self.name_two, self.age)

# objc = Child(27)
# objc.display()
