# Import the dataclass decorator
from dataclasses import dataclass

# Define a dataclass
@dataclass #automatically generates an __init__ method, a __repr__ method
class Student:
    name: str
    age: int
    grade: str

# Create instances of the Student class
student1 = Student("Alice", 18, "A")
student2 = Student("Bob", 17, "B")

# Access attributes of the instances
print(f"Student 1: {student1.name}, Age: {student1.age}, Grade: {student1.grade}")
print(f"Student 2: {student2.name}, Age: {student2.age}, Grade: {student2.grade}")