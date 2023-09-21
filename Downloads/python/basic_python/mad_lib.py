# Mad Libs Generator

# Function to collect user inputs
def get_user_inputs():
    adjective = input("Enter an adjective: ")
    pronoun = input("Enter a pronoun: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")

    return adjective, pronoun, noun, verb

# Function to generate the Mad Lib story
def generate_mad_lib(adjective, pronoun, noun, verb):
    story = f"Once upon a time, there was a {adjective} {noun} named {pronoun}. "
    story += f"{pronoun} loved to {verb} all day long. "
    story += f"Everyone in the {noun}'s town admired {pronoun}'s {adjective} personality."
    
    return story

# Main program
if __name__ == "__main__":
    print("Welcome to the Mad Libs Generator!")
    
    # Get user inputs
    adj, pro, n, v = get_user_inputs()
    
    # Generate and display the story
    mad_lib_story = generate_mad_lib(adj, pro, n, v)
    print("\nHere's your Mad Lib story:\n")
    print(mad_lib_story)