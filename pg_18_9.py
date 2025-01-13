# -----------------------------------------------
class Complex:
    count = 0

    def __init__(self, r=0.0, i=0.0):
        self.real = r
        self.imag = i
        print(self.real, self.imag)

        Complex.count += 1
        print('This is {} run to __init__()'.format(Complex.count))

    def __eq__(self, other):
        if self.real == other.real and self.imag == other.imag:
            print('if block')
            print(self.real, self.imag)
            print(other.real, other.imag)
            return True
        else:
            print('else block')
            print(self.real, self.imag)
            print(other.real, other.imag)
            return False

c1 = Complex(1.1, 0.2)
c2 = Complex(1.1, 0.2)
c3 = Complex(1.1, 0.2)
c4 = Complex(2.1, 0.4)
c5 = Complex(1.1, 0.2)

if c1 == c2 == c3 == c4 == c5:
    print('Match')
else:
    print('No Match')
