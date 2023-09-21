# Input the string and delimiter from the user
input_string = input("Enter a string: ")
delimiter = input("Enter a delimiter: ")

# Initialize lists to store the string and delimiter parts
string_list = []
delimiter_list = []

# Split the input string using the provided delimiter
parts = input_string.split(delimiter)

# Iterate through the parts and determine whether each part is a string or delimiter
for i, part in enumerate(parts):
    if i % 2 == 0:
        # Even-indexed parts are strings
        string_list.append(part)
    else:
        # Odd-indexed parts are delimiters
        delimiter_list.append(part)

# Print the resulting lists
print("String parts:", string_list)
print("Delimiter parts:", delimiter_list)