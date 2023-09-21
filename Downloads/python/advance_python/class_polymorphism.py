class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

def animal_says(animal):
    print(animal.speak())

# Create instances of different animals
dog = Dog()
cat = Cat()
cow = Cow()

# Demonstrate polymorphism
animal_says(dog)  # Output: "Woof!"
animal_says(cat)  # Output: "Meow!"
animal_says(cow)  # Output: "Moo!"