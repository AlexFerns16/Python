# class Employee:
#     def set_data(self, n, a, s):
#         self.name = n
#         self.age = a
#         self.salary = s

#     def display(self):
#         print(self.name, self.age, self.salary)

# obj_one = Employee()

# # x = 5

# obj_one.set_data('John', 27, 70000)
# obj_one.display()

# class Employee:
#     def __init__(self, n, a, s):
#         self.name = n
#         self.age = a
#         self.salary = s

#     def display(self):
#         print(self.name, self.age, self.salary)

# obj_one = Employee('Thomas', 29, 90000)     # add: #123 > 'Thomas', 29, 90000
# obj_one.display()

# obj_two = Employee('John', 24, 50000)       # add: #456 > 'John', 24, 50000
# obj_two.display()






# single inheritance
# multilevel inheritance
# multiple inheritane
# hierarchial inheritance

# single inheritance

# class Parent:
#     def __init__(self):
#         self.name = 'John'

# class Child(Parent):
#     def display(self):
#         print(self.name)

# obj_child_one = Child()
# obj_child_one.display()


# multilevel inheritance

class Parent:
    def __init__(self):
        self.name = 'John'

class Child(Parent):
    def __init__(self):
        self.age = 27
        Parent.__init__(self)

class GChild(Child):
    def __init__(self):
        self.salary = 70000
        Child.__init__(self)

    def display(self):
        print(self)
        print(self.salary, self.age, self.name)

obj_gc_one = GChild()
obj_gc_one.display()

print(obj_gc_one)
