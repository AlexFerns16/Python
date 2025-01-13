# abstract classes

from abc import ABC, abstractclassmethod
class Shape(ABC):
    @abstractclassmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print('In Rectangle.draw')

class Circle(Shape):
    def draw(self):
        print('In Circle.draw')

# s = Shape()

r = Rectangle()
r.draw()

c = Circle()
c.draw()
