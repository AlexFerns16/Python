# object initialization

class employee():
    def set_data(self, n, a, s):
        self.name = n
        self.age = a
        self.salary = s

    def display(self):
        print(self.name, self.age, self.salary)

    def __init__(self, n='', a=0, s=0.0):
        self.name = n
        self.age = a
        self.salary = s

    def __del__(self):
        print('destructor is executed')

# e1 = employee()
# e1.set_data('Suresh', 25, 30000)
# e1.display()

e2 = employee('Ramesh', 23, 25000)
e2.display()

# e3 = employee()
# e3.display()

# e2 = None
# e2.display()

print(e2.name)
