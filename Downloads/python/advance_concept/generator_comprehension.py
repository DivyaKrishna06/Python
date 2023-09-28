numbers = [1, 2, 3, 4, 5]

# Create a generator comprehension
squared_numbers_generator = (num ** 2 for num in numbers)

for squared_num in squared_numbers_generator:
    print(squared_num)