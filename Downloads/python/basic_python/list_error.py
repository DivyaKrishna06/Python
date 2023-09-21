# Function to perform the operation on the list
def perform_operation(lst, index):
    try:
        result = lst[index]  # Replace this with your desired operation
        print(f"Result of the operation at index {index}: {result}")
    except IndexError:
        print("Index is out of range.")

# Get user input for the list
try:
    input_list = input("Enter a list of values (comma-separated): ").split(',')
    input_list = [int(item.strip()) for item in input_list] #returns a copy of the string by removing both the leading and the trailing characters
except ValueError:
    print("Invalid input. Please enter a list of integers.")
    exit(1)

# Get user input for the index
try:
    index = int(input("Enter an index to perform the operation: "))
except ValueError:
    print("Invalid input. Please enter an integer index.")
    exit(1) # terminated due to application error

# Call the function to perform the operation
perform_operation(input_list, index)