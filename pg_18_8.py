# -------------------------------------
class Fruit:
    count = 0           # class variable

    def __init__(self, n, q, c):
        self.name = n
        self.quantity = q
        self.color = c
        Fruit.count += 1

    def display(self):
        print(Fruit.count)

    def disp():
        print('Hello')

f1 = Fruit('Apple', 5, 'Red')
f1.display()

f2 = Fruit('Mango', 7, 'Yellow')
f2.display()

# ----------------------------------------------------------------------------------
print(f1.count)

Fruit.disp()    # display() without argument in class can be called using class name
