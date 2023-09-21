import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

try:
    radius = float(input("Enter the radius of the circle: "))
    if radius < 0:
        print("Radius cannot be negative.")
    else:
        circle = Circle(radius)
        area = circle.calculate_area()
        perimeter = circle.calculate_perimeter()
        print(f"Area of the circle: {area:.2f}")
        print(f"Perimeter of the circle: {perimeter:.2f}")
except ValueError:
    print("Invalid input. Please enter a valid number for the radius.")