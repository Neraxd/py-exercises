# Text Analyzer
# Ask for a sentence.
# Print:
# Number of characters
# Number of words
# First 5 characters
# Last 5 characters


sentence = input("Please enter a phrase: ")

char_count = len(sentence)
words = sentence.split()
word_count = len(words)
first_5 = sentence[:5]
last_5 = sentence[-5:]
print(
    f"Characters: {char_count} | Words: {word_count} | First 5: '{first_5}' | Last 5: '{last_5}'"
)
