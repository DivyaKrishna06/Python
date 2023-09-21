# Function to remove duplicates from a list
def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Input from the user
user_input = input("Enter elements of the list separated by spaces: ")
user_list = user_input.split()  # Split the input string into a list

# Convert the input elements to their appropriate data types (e.g., int, float) if needed
# For example, you can use a list comprehension like this:
# user_list = [int(item) for item in user_list]

# Remove duplicates from the user's list
result_list = remove_duplicates(user_list)

# Print the list with duplicates removed
print("List with duplicates removed:", result_list)
