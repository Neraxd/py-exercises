# Write a function can_vote(age) that returns a boolean:

# Return age >= 18

def vote (age) :
    return age >= 18


valid = vote(18)
not_valid = vote(10)

print(valid,not_valid)