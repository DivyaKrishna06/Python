class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            # Add two Point objects
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Point(new_x, new_y)
        else:
            raise TypeError("Unsupported operand type for +: Point and {}".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, Point):
            # Subtract two Point objects
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Point(new_x, new_y)
        else:
            raise TypeError("Unsupported operand type for -: Point and {}".format(type(other)))

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2
print("p1 + p2 =", p3)

p4 = p2 - p1
print("p2 - p1 =", p4)

print("p1 == p2:", p1 == p2)