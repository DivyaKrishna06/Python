class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

def custom_function(value):
    if value < 0:
        raise MyCustomException("Value cannot be negative")

try:
    user_input = int(input("Enter a number: "))
    custom_function(user_input)
except MyCustomException as e:
    print(f"Custom Exception: {e}")
except ValueError:
    print("Invalid input. Please enter a valid number.")