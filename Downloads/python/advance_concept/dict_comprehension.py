# Dictionary comprehension with 'if' condition
person_data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

filtered_data = {key: value for key, value in person_data.items() if key.startswith('a')}

print("Original dictionary:", person_data)
print("Filtered dictionary:", filtered_data)

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

odd_numbers = {x for x in numbers if x % 2 != 0}

print("Original set:", numbers)
print("Odd numbers:", odd_numbers)