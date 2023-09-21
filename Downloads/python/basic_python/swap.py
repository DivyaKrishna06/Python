# Input two variables
variable1 = input("Enter the first variable: ")
variable2 = input("Enter the second variable: ")

# Display the original values
print("Original values:")
print("Variable 1:", variable1)
print("Variable 2:", variable2)

# Swap the variables using a temporary variable
temp = variable1
variable1 = variable2
variable2 = temp

# Display the swapped values
print("\nAfter swapping:")
print("Variable 1:", variable1)
print("Variable 2:", variable2)