# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}, and I'm {self.age} years old.")

# Subclass 1
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

# Subclass 2
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

# User interactive data input
name = input("Enter name: ")
age = int(input("Enter age: "))
role = input("Are you a Student or a Teacher? ")

if role.lower() == "student":
    student_id = input("Enter student ID: ")
    student = Student(name, age, student_id)
    student.introduce()
    student.study()
elif role.lower() == "teacher":
    subject = input("Enter subject: ")
    teacher = Teacher(name, age, subject)
    teacher.introduce()
    teacher.teach()
else:
    print("Invalid role entered. Please enter 'Student' or 'Teacher'.")
