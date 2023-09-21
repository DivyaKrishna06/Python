# Original list of tuples
original_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Sorting the list of tuples based on the second element (numeric value)
sorted_list = sorted(original_list, key=lambda x: x[1])

# Display the sorted list
print("Sorting the List of Tuples:")
print(sorted_list)