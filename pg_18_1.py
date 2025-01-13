# classes and objects

class Employee():
    def set_data(self, n, a, s):
        self.name = n
        self.age = a
        self.salary = s

    def display_data(self):
        print(self.name, self.age, self.salary)
        print(id(self))
        print(id(self.name))

e1 = Employee()
e1.set_data('Ramesh', 23, 25000)
e1.display_data()
print(id(e1))

# e2 = Employee()
# e2.set_data('Suresh', 25, 30000)
# e2.display_data()
# print(id(e2))

a = 5
print(id(a))

b = 5
print(id(b))

# class int:
#     def __init__(self):
#         self -> int

#     def display(self):
#         print(self.var)

# class str:
#     def upper(self):
#         self.up = 0
