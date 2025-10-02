# Mini Quiz Game 🧠

# Ask 3 questions.

# Track score (each correct answer = +1).

# Print final score with percentage.

q1 = input("what color is an elephant? : ").lower()
q2 = input("who was the fist president of the united states of america? : ").lower()
q3 = input("who is the current president of the united states of america? : ").lower()

score = 0

if q1 == "grey" or q1 == "gray":
    score += 1

if q2 == "george washington":
    score += 1

if q3 == "donald trump":
    score += 1

print(f"your final score is : {score} corrects ({ int((score / 3) * 100): }%)")
