# -----------------------------------------------
class Complex:
    count = 0

    def __init__(self, r=0.0, i=0.0):
        self.real = r
        self.imag = i
        print(self.real, self.imag)

        Complex.count += 1
        print('This is {} run to __init__()'.format(Complex.count))

    def __add__(self, other):
        print('add operator')
        z = Complex()
        print('address of z is {}'.format(z))
        print('object z')
        z.real = self.real + other.real
        z.imag = self.imag + other.imag
        print(self.real, self.imag)
        print(other.real, other.imag)
        print(z.real, z.imag)
        return z

    def display(self):
        print(self.real, self.imag)

c1 = Complex(1.1, 0.2)
c2 = Complex(1.2, 0.3)
c3 = Complex(1.3, 0.4)

# c3 = c1 + c2
# c3.display()

c4 = c1 + c2 + c3
print('address of c4 is {}'.format(c4))     # same as the last updated address of 'z'
c4.display()
