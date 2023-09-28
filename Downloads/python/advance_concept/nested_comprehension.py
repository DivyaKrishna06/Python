# Nested List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [num for row in matrix for num in row]

# Nested Dictionary Comprehension
original_dict = {'a': 1, 'b': 2, 'c': 3}
squared_dict = {key: value ** 2 for key, value in original_dict.items()}

# Nested Set Comprehension
sets_of_numbers = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}]
unique_numbers = {num for set_nums in sets_of_numbers for num in set_nums}

print("Flattened Matrix:", flattened_matrix)
print("Squared Dictionary:", squared_dict)
print("Unique Numbers:", unique_numbers)