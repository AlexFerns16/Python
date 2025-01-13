# create outer class
class Doctors:
    def __init__(self):
        self.name = 'Doctor'
        print(1)
        # self.den = self.Dentist()
        self.den = Doctors.Dentist()
        print(3)
        print(self.den)
        self.car = self.Cardiologist()
        print(5)

    def show(self):
        print('In outer class')
        print('Name:', self.name)

    # create a 1st Inner class
    class Dentist:
        def __init__(self):
            print(2)
            print(self)
            # z = Doctors.Dentist()             # debug
            self.name = 'Dr. Savita'
            self.degree = 'BDS'

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)

    # z = Dentist()                             # debug

    # create a 2nd Inner class
    class Cardiologist:
        def __init__(self):
            print(4)
            self.name = 'Dr. Amit'
            self.degree = 'DM'

        def display(self):
            print("Name:", self.name)
            print("Degree:", self.degree)


# create an object
# of outer class
outer = Doctors()
outer.show()

# create an object
# of 1st inner class
d1 = outer.den

# create an object
# of 2nd inner class
d2 = outer.car

print()
d1.display()

print()
d2.display()

print('test')
print(id(type('Python')))
print(id(type('Cython')))
