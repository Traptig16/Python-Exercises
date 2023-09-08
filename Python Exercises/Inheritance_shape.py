import math
class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def area(self):
        pass

    def perimeter(self):
        pass

    def shape(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def shape(self):
        return "Circle"

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def shape(self):
        return "Rectangle"

class Triangle(Shape):
    def __init__(self, color, base, height, side1, side2):
        super().__init__(color)
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.base + self.side1 + self.side2

    def shape(self):
        return "Triangle"
length=int(input("enter length"))
width=int(input("enter width"))
color=input('color')

rectangle=Rectangle(color, length, width)
print(f"Shape: {rectangle.shape()}")
print(f"Color: {rectangle.get_color()}")
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")