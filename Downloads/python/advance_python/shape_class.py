import math

class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return 4 * self.side

# Input from the user
shape_type = input("Enter the type of shape (circle, triangle, square): ").lower()

if shape_type == "circle":
    radius = float(input("Enter the radius of the circle: "))
    shape = Circle(radius)
elif shape_type == "triangle":
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))
    shape = Triangle(side1, side2, side3)
elif shape_type == "square":
    side = float(input("Enter the length of a side of the square: "))
    shape = Square(side)
else:
    print("Invalid shape type")
    shape = None

if shape:
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")