import random

# Define the moves
moves = ["Rock", "Paper", "Scissors"]

# Function to get the user's move
def get_user_move():
    while True:
        user_choice = input("Enter your move (Rock, Paper, or Scissors): ").capitalize()
        if user_choice in moves:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

# Function to get the computer's move
def get_computer_move():
    return random.choice(moves)

# Function to determine the round winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win this round!"
    else:
        return "Computer wins this round!"

# Initialize scores
user_score = 0
computer_score = 0

# Play the game
rounds_to_play = int(input("How many rounds do you want to play? "))
for _ in range(rounds_to_play):
    user_choice = get_user_move()
    computer_choice = get_computer_move()
    
    print(f"You chose {user_choice}. Computer chose {computer_choice}.")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    if "You win" in result:
        user_score += 1
    elif "Computer wins" in result:
        computer_score += 1

# Determine the final winner
if user_score > computer_score:
    print("You are the overall winner!")
elif computer_score > user_score:
    print("Computer is the overall winner!")
else:
    print("It's a tie overall!")

print(f"Final Score - You: {user_score}, Computer: {computer_score}")