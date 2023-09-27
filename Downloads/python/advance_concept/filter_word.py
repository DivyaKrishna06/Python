# Function to filter
def filter_short_words(word_list):
    return filter(lambda word: len(word) >= 4, word_list)

user_input = input("Enter a list of words separated by spaces: ")
words = user_input.split()

filtered_words = list(filter_short_words(words))

print("Words longer than or equal to 4 letters:") # printing filtered list 
for word in filtered_words:
    print(word)