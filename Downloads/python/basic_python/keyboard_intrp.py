try:
    user_input = input("Enter a number: ")
except KeyboardInterrupt:
    print("\nInput canceled by the user.")
else:
    try:
        number = float(user_input)
        print(f"You entered the number: {number}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")