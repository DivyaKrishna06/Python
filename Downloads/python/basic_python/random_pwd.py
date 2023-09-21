import random
import string

def generate_random_password(words, length=12):
    # Combine user input words
    user_input = ''.join(words)
    
    # Generate random characters for the remaining length
    remaining_length = max(length - len(user_input), 0)
    random_chars = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))
    
    # Shuffle the combined string
    combined_string = user_input + random_chars
    password_list = list(combined_string)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

# Get user input words
user_words = input("Enter words (separated by spaces) to include in your password: ").split()

# Set the desired password length
password_length = int(input("Enter the desired password length: "))

# Generate and print the random password
random_password = generate_random_password(user_words, password_length)
print("Your random password is:", random_password)