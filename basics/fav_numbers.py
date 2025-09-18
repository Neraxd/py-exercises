# Favorite Numbers
# Make a list of 6 numbers.
# Print the slice containing the 2nd to 4th numbers.
# Remove the last number.
# Insert a new number at index 2.

numbers = [10, 7, 11, 6, 1, 0]

print(f"the slice of 2-4 : {numbers[2:5]}")

numbers.pop()
numbers.insert(2, 67)
