def repeat_string(input_string, n):
    # Check if n is a non-negative integer
    if not isinstance(n, int) or n < 0:
        return "Invalid input. Please provide a non-negative integer for 'n'."
    
    # Use string multiplication to repeat the input string n times
    result_string = input_string * n
    return result_string

# Get input from the user
input_string = input("Enter a string: ")
n = int(input('Enter the number of copies (a non-negative integer): '))

# Call the function and print the result
result = repeat_string(input_string, n)
print("Result:", result)