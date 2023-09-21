class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade} \n")

# Function to get user input for a new student
def get_student_input():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")
    return name, age, grade

# Create a list to store student objects
students = []

# Interactive loop to add students and display their info
while True:
    choice = input("Do you want to add a new student (yes/no)? ").lower()
    
    if choice == "yes":
        name, age, grade = get_student_input()
        student = Student(name, age, grade)
        students.append(student)
        print("Student added successfully!")
    elif choice == "no":
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

# Display information for all the students
print("\nStudent Information:\n")
for student in students:
    student.display_student_info()
