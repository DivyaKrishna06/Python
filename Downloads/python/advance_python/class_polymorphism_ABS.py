from abc import ABC, abstractmethod

# Define an abstract base class (ABC)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Create concrete subclasses that inherit from the Shape ABC
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Create a function that accepts any Shape and calculates its area
def calculate_area(shape):
    if isinstance(shape, Shape):
        return shape.area()
    else:
        return "Invalid shape"

# Create instances of different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Calculate and print their areas using polymorphism
print(f"Circle Area: {calculate_area(circle)}")
print(f"Rectangle Area: {calculate_area(rectangle)}")
print(f"Triangle Area: {calculate_area(triangle)}")