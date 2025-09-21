# For loops - Exercise
# Party invitation
#
# - You’re having a party and want to invite your friends.
# - You want the print out invitations for each friend using for loops
# - The names are in two lists, ‘names’ and ‘names1’
# - You also need to add two extra names to the list using an ‘input’ box, when you run the code
# - Printout one invitation to each friend per line
# - Names should be properly capitalized
#
# Example of printout:
# John Cleese! You are invited to the party on saturday.
# Eric Idle! You are invited to the party on saturday.
#
# - Hint: you may need two (for) loops to solve this exercise


names = ["john ClEEse", "Eric IDLE", "michael"]
names1 = ["graHam chapman", "TERRY", "terry jones"]
names.extend(names1)

for i in range(2):
    added_names = input(f"enter number {i} name :")
    names.append(added_names)


for name in names:

    print(f"{name.title()}! You are invited to the party on saturday.")
