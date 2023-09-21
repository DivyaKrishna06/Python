class Person:
    def __init__(self, name, age): # __init__ method (constructor) that initializes the name and age 
        self.name = name
        self.age = age

    def introduce(self):  #class- method
        return f"My name is {self.name} and I am {self.age} years old."
# end of class

def create_person():
    name = input("Enter the person's name: ")
    age = input("Enter the person's age: ")

    try:
        age=int(age)
        person = Person(name, age) # Create a Person object
        return person
    except ValueError:
        print("Invalid age. Please enter a valid integer for age.")
        return create_person() # Recursively call the function if age is not valid

# if __name__ == "__main__": #  is used to execute some code only if the file was run directly, and not imported.
#     person = create_person()
#     print(person.introduce())

print("Welcome to the Person Class Program!")

while True:
    print("\nOptions:")
    print("1. Create a person")
    print("2. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        person = create_person()
        if person:
            print("\nPerson created successfully!")
            print(person.introduce())
    elif choice == '2':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a valid option.")
