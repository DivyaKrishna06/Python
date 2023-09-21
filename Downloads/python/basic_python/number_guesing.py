import random

def main():
    # Set the range for the random number
    min_num = 1
    max_num = 100
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    max_attempts = 10  # You can adjust this to change the difficulty
    
    print("Welcome to the Number Guessing Game!")
    print(f"Guess the number between {min_num} and {max_num}. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess < min_num or guess > max_num:
            print(f"Your guess should be between {min_num} and {max_num}. Try again.")
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

    if attempts >= max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    main()