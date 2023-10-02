class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

def divide(a, b):
    if b == 0:
        raise CustomException("Division by zero is not allowed.")
    return a / b

try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    
    result = divide(num1, num2)
    print(f"Result of division: {result}")
except CustomException as ce:
    print(f"Custom Exception: {ce}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")