# Using list comprehension
values = [(x, y) for x in range(5) for y in range(3)]

# Equivalent code using nested for loops
values_nested = []
for x in range(5):
    for y in range(3):
        values_nested.append((x, y))

# Check if both methods produce the same result
print(values == values_nested)  # Should print True