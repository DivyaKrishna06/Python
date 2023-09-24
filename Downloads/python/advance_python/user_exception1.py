# Define a custom exception class
class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

# Function that raises the custom exception
def divide(a, b):
    if b == 0:
        raise MyCustomException("Division by zero is not allowed")
    return a / b

# Main program
try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    
    result = divide(num1, num2)
    print(f"Result of division: {result}")
    
except ValueError:
    print("Invalid input. Please enter valid numbers.")
except MyCustomException as e:
    print(f"Custom Exception: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")