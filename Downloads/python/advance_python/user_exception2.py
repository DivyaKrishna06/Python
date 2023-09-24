class InvalidInputError(Exception):
    def __init__(self, message="Invalid input"):
        self.message = message
        super().__init__(self.message)

def calculate_square_root(num):
    if num < 0:
        raise InvalidInputError("Negative numbers are not allowed")
    return num ** 0.5

try:
    num = float(input("Enter a number: "))
    result = calculate_square_root(num)
    print(f"The square root of {num} is {result}")
except InvalidInputError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Please enter a valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")