# Accept an integer input from the user
n = int(input("Enter an integer (n): "))

# Calculate nn and nnn
nn = n * 10 + n
nnn = nn * 10 + n

# Calculate the final result
result = n + nn + nnn

# Display the result
print(f"The result of {n} + {nn} + {nnn} is {result}")