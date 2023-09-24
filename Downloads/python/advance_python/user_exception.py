# Define a custom exception class
class ValueTooHighError(Exception):
    def __init__(self, value, limit):
        self.value = value
        self.limit = limit
        self.message = f"Value {value} is too high. It should be less than or equal to {limit}"
        super().__init__(self.message)

# Function to check if a value exceeds the limit
def check_value(value, limit):
    if value > limit:
        raise ValueTooHighError(value, limit)
    else:
        print(f"Value {value} is within the allowed limit of {limit}")

try:
    limit = 100
    user_value = int(input("Enter an integer value: "))
    check_value(user_value, limit)
except ValueTooHighError as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a valid integer.")