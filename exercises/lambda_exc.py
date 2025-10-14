# 🧠 Exercise: Lambda Transformations Challenge
#
# Goal:
# Practice writing and using lambda functions with map(), filter(), and sorted().
#
# Given a list of dictionaries representing students:
# [
#     {"name": "Ilia", "score": 85},
#     {"name": "Sara", "score": 92},
#     {"name": "Omid", "score": 76},
#     {"name": "Lina", "score": 58},
# ]
#
# 🧩 Requirements:
# 1. Use `filter()` with a lambda to keep only students who passed (score >= 60).
# 2. Use `map()` with a lambda to turn each student into a formatted string like:
#    "Ilia: 85 points"
# 3. Use `sorted()` with a lambda key to sort students by score (descending order).
# 4. Print all three results clearly.
#
# 🧪 Mini challenges:
# - Try adding a second sorting criterion (e.g., by name alphabetically if scores are equal).
# - Add a bonus: use a lambda inside `max()` to find the top student.
#
# 🚀 Goal: Do all of this **without defining any normal functions (def)** — only lambdas!

our_list = [
    {"name": "Ilia", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "Omid", "score": 76},
    {"name": "Lina", "score": 58},
]

# filter
passed = list(filter(lambda x: x["score"] >= 60, our_list))

# map
formatted_string = list(map(lambda x: f"{x["name"]} : {x["score"]} points", passed))
print(formatted_string)  # or we could pass the orginial data
for f in formatted_string:
    print(f)


# sorted
sorted_scores = sorted(our_list, key=lambda x: (-x["score"], x["name"]))
print("\nSorted by score (desc) then name:")
for s in sorted_scores:
    print(s)


# max
top_student = max(
    our_list,
    key=lambda x: x["score"],
)
print(top_student)
