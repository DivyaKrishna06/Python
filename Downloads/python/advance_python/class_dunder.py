class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass instance with value: {self.value}"

    def __add__(self, other):
        if isinstance(other, MyClass):
            return MyClass(self.value + other.value)
        elif isinstance(other, int):
            return MyClass(self.value + other)
        else:
            raise ValueError("Unsupported operand type")

    def __eq__(self, other):
        if isinstance(other, MyClass):
            return self.value == other.value
        return False

# Create instances of MyClass
obj1 = MyClass(5)
obj2 = MyClass(10)

# Testing __str__ method
print(obj1)  # Output: MyClass instance with value: 5

# Testing __add__ method
result = obj1 + obj2
print(result)  # Output: MyClass instance with value: 15

result = obj1 + 3
print(result)  # Output: MyClass instance with value: 8

# Testing __eq__ method
print(obj1 == obj2)  # Output: False
print(obj1 == MyClass(5))  # Output: True