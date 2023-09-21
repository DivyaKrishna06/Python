from itertools import combinations

# Get user input for a list of digits
user_input = input("Enter a list of digits separated by spaces: ")
digits = user_input.split()

# Ensure there are at least 3 digits
if len(digits) < 3:
    print("You need to enter at least 3 digits.")
else:
    # Generate combinations of 3 digits
    digit_combinations = list(combinations(digits, 3))

    # Print the combinations
    print("Combinations of 3 digits:")
    for combination in digit_combinations:
        print(" ".join(combination))