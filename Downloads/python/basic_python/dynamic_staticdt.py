# Static Data Type Example (Using Type Hints)
name: str = "John"  # The variable 'name' is explicitly annotated as a string (str).

age: int = 30      # The variable 'age' is explicitly annotated as an integer (int).

# Dynamic Data Type Example
city = "New York"  # Python dynamically assigns the type str to the variable 'city'.

price = 19.99      # Python dynamically assigns the type float to the variable 'price'.

# Check the data types
def check_data_type(variable_name, value):
    data_type = type(value).__name__
    print(f"The data type of {variable_name} is {data_type}")

check_data_type("name", name)
check_data_type("age", age)
check_data_type("city", city)
check_data_type("price", price)