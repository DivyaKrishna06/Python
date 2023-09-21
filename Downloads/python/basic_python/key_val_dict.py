# Creating an empty dictionary
my_dict = {}

# Adding key-value pairs to the dictionary
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['city'] = 'New York'

# Accessing values using keys
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])

# Modifying a value
my_dict['age'] = 31

# Iterating through the dictionary
print("\nIterating through the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Removing a key-value pair
del my_dict['city']

# Checking if a key exists in the dictionary
if 'city' not in my_dict:
    print("\n'city' key is not in the dictionary.")

# Checking the length of the dictionary
print("\nNumber of key-value pairs in the dictionary:", len(my_dict))