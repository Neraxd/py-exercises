# Create a file called notes.txt with the following lines:

# Python is fun
# I am learning file handling
# End of notes

# Write a Python program that reads this file and prints only the first and last line.

notes_file = open("/home/ilia/Documents/Python/files/notes.txt", "r")

lines_list = notes_file.readlines()
first_line = lines_list[0]
last_line = lines_list[-1]

print(f"first : {first_line} \nlast : {last_line} ")

notes_file.close()
