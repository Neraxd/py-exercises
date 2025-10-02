# Word Counter
# Take a sentence as input.
# Count how many times each word appears (use a dictionary).
# Print them sorted by frequency (highest first).

sentence = input("Please enter a phrase : ")
sentence = sentence.split()
count_dict = {}


for word in sentence :
    count_dict.update({word: sentence.count(word)})

sorted_counts = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)
print(sorted_counts)