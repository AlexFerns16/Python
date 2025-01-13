# access convention

class Employee():
    def set_data(self, n, a, s):
        self.name = n
        self.age = a
        self.salary = s

    def display_data(self):
        print(self.name, self.age, self.salary)

# ---------------------------------------------
obj_one = Employee()

obj_one.name = 'Ajay'
print(obj_one.name)

obj_one.age = 24
print(obj_one.age)

obj_one.salary = 50000
print(obj_one.salary)

# ---------------------------------------------
obj_two = Employee()

obj_two.name = 'Rakesh'
print(obj_two.name)

obj_two.age = 28
print(obj_two.age)

obj_two.salary = 70000
print(obj_two.salary)

# ---------------------------------------------
var = obj_one.age + obj_two.age
print(var)
