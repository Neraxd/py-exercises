# 1. Ask how many people are entering the raffle (at least 3 names).
# 2. Use a loop to collect their names into a list.
# 3. Ask for exactly 3 prize names (in order) and store them in a list.
# 4. Randomly pick 3 different winners from the participant list.
# 5. Print out who wins which prize and make sure the final one
#    is clearly marked as the Grand Prize. 🏆
#
# Hint: Use loops, lists, and a tool that picks random items without repeats.
import random

names = []
prizes = []

people = int(input("How many people are entering the raffle? "))

if people < 3:
    print("At least three people are needed! ")
    exit()


for i in range(people):
    person = input(f"Please enter the names!\nParticipant number {i+1}: ")
    names.append(person)
for i in range(3):
    prize = input(f"Please enter the prizes!\nprize number {i+1}: ")
    prizes.append(prize)
    random_winners = random.sample(names, k=3)
    final_winners = list(zip(random_winners, prizes))
    print("======*** Raffle Results ***======")
    print(f"Number of participants: {people}")

for name, prize in final_winners:

    if name == random_winners[-1]:
        print(f"{name} has won the grand prize which is {prize} !")
    else:
        print(f"{name} has won {prize}")
