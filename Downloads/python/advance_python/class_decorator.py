# Define a decorator function
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the method is called")
        result = func(*args, **kwargs)
        print("After the method is called")
        return result
    return wrapper

# Create a class with a decorated method
class MyClass:
    def __init__(self, value):
        self.value = value

    @my_decorator
    def my_method(self):
        print(f"My method is called with value: {self.value}")

# Create an instance of the class
obj = MyClass(42)

# Call the decorated method
obj.my_method()