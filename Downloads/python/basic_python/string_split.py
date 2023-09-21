# Get the input string from the user
input_string = input("Enter a string: ")

# Get the delimiter from the user
delimiter = input("Enter the delimiter to split the string: ")

# Split the input string into a list using the specified delimiter
split_list = input_string.split(delimiter)

# Print the resulting list
print("Split variables:")
for index, variable in enumerate(split_list, start=1):
    print(f"Variable {index}: {variable}")