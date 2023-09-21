# Base class: Animal
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass  # This method will be overridden in derived classes

# Derived class 1: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def speak(self):
        return f"{self.name} (Dog) says Woof!"

# Derived class 2: Cat
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def speak(self):
        return f"{self.name} (Cat) says Meow!"

# User interaction
def main():
    print("Welcome to the Animal Inheritance Program!")
    animal_type = input("Enter the animal type (Dog or Cat): ").capitalize()

    if animal_type == "Dog":
        name = input("Enter the dog's name: ")
        breed = input("Enter the dog's breed: ")
        dog = Dog(name, breed)
        print(dog.speak())
    elif animal_type == "Cat":
        name = input("Enter the cat's name: ")
        color = input("Enter the cat's color: ")
        cat = Cat(name, color)
        print(cat.speak())
    else:
        print("Invalid animal type. Please enter 'Dog' or 'Cat'.")

if __name__ == "__main__":
    main()