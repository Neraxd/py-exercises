# Requirements:
# Create a list of student names and a list of topics.
# Randomly assign each student a topic.
# Pair students and topics using zip/unzip.
# Make a small custom module (separate .py file) with a helper function that formats the assignment (e.g. "Alice → Math").
# In your main program, import and use that function.
# Use a lambda inside sorted() to order results by topic.
# Store the final results in a dictionary comprehension.
# Print all results.
# modules
import random
from seprate import helper

# datas
students = ["eric garcia", "johnson sttaham", "john pork", "george floyd"]
topics = ["math", "history", "science", "english"]
# random topic selection
random_topics = random.sample(topics, k=len(topics))
pairing = list(zip(students, random_topics))

# sorted datas =>  three differents approach

helper_func = helper(pairing)
sorted_data = sorted(pairing, key=lambda item: item[-1])
final_dict = {std: topic for std, topic in sorted_data}


# printing the result

print(f"this is the sorted data using lambda :\n{sorted_data}\n")
print(f"this is the sorted data using helper module :\n{helper_func}\n")
print(f"this is the sorted data using dictionary comprehension :\n{final_dict}\n")



