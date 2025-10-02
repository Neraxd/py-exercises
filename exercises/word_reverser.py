# Word Reverser

# Ask for a sentence.

# Print the sentence reversed, and also print only the first and last words.

sentence = input("please enter a pharse: ")

reversed_sentence = sentence[::-1]
splitted_sentence = sentence.split()
first_word = splitted_sentence[0]
last_word = splitted_sentence[-1]


print(
    f"reversed: {reversed_sentence} , first word : {first_word} , last word : {last_word}"
)
