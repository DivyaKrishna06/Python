numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension to create a new list containing the squares of even numbers
squares_of_evens = [x**2 for x in numbers if x % 2 == 0]

# List comprehension to create a new list containing the cubes of odd numbers
cubes_of_odds = [x**3 for x in numbers if x % 2 != 0]

# Dictionary comprehension to create a dictionary mapping numbers to their squares
squares_dict = {x: x**2 for x in numbers}

# Print the results
print("Original List:", numbers)
print("Squares of Evens:", squares_of_evens)
print("Cubes of Odds:", cubes_of_odds)
print("Squares Dictionary:", squares_dict)