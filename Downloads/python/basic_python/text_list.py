# Define a long text
long_text = input('Enter a long text: ')
# """
# This is a sample text that we will use to demonstrate
# how to count the frequency of each word in this text.
# The words in this text will be split and counted.
# """

# Split the text into words
words = long_text.split()

# Create a dictionary to store word frequencies
word_frequencies = {}

# Iterate through the list of words and update the dictionary
for word in words:
    # Remove punctuation and convert to lowercase (optional)
    word = word.strip('.,!?"\'').lower()
    
    # Increment the word count in the dictionary
    if word in word_frequencies:
        word_frequencies[word] += 1
    else:
        word_frequencies[word] = 1

# Print the words and their frequencies
for word, frequency in word_frequencies.items():
    print(f'Word: {word}, Frequency: {frequency}')