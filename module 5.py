import math


class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")

    def describe(self):
        return (
            f"A {self.color} shape with area {self.area():.2f} "
            f"and perimeter {self.perimeter():.2f}"
        )


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        semi = (self.a + self.b + self.c) / 2
        return math.sqrt(
            semi
            * (semi - self.a)
            * (semi - self.b)
            * (semi - self.c)
        )


class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)


def largest_shape(shapes):
    largest = shapes[0]

    for shape in shapes:
        if shape.area() > largest.area():
            largest = shape

    return largest


# Test Shape and NotImplementedError
s = Shape("red")

try:
    s.area()
except NotImplementedError as e:
    print(e)


# Test Circle
c = Circle("blue", 5)
print(c.area())
print(c.perimeter())
print(c.describe())


# Test Rectangle
r = Rectangle("green", 4, 6)
print(r.describe())


# Test Triangle
t = Triangle("yellow", 3, 4, 5)
print(t.area())
print(t.perimeter())
print(t.describe())


# Demonstrate polymorphism
shapes = [
    Circle("red", 3),
    Rectangle("green", 4, 6),
    Triangle("blue", 3, 4, 5),
]

for shape in shapes:
    print(shape.describe())


# Test Square
sq = Square("purple", 5)
print(sq.describe())


# Test largest_shape
biggest = largest_shape(shapes)
print(f"Largest shape: {biggest.describe()}")