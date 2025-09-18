# High Score Tracker
# Print the highest score.
# Print the lowest score.
# Add a new score 88.
# Sort the list and print it.


scores = [50, 80, 92, 66, 75]
highest_score = max(scores)
lowest_score= min(scores)

print(f"highest score is : {highest_score} ")
print(f"lowest score is : {lowest_score} ")
scores.append(88)
scores.sort()

print(f"final list : {scores}")