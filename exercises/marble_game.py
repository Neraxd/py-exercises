# Trading Game simulation
#
# Create a marble betting game:
#
# - Draw a marble from a bag (assume it’s random)
# - A bag has 10 marbles: 6 green and 4 red
# - If you draw a green marble you win the same amount that you bet,
#   if you draw a red marble you lose the amount you bet.
# - Marbles are replaced into the bag after each round
# - Before each draw decide how much you will bet and enter it
# - You start the game with 1,000 gold pieces or $, £, €
# - The number of rounds/draws should be variable
# - If you lose half of your money, the game is over
# - Print/show out data as you go along,
#   and remember you have to print data in the input prompt
#   (as printouts are not seen in Scrimba when code is running)
#
# Bonus:
# - Replace two marbles:
#     1 green → black marble (10X winner)
#     1 red   → white marble (5X loser)
import random

money = float(1000)
half = money / 2
rounds = 4
bag = ["green"] * 5 + ["red"] * 3 + ["black"] + ["white"]


for i in range(rounds):

    marble = random.choice(bag)
    print(f"===== Round {i+1} =====")
    bet = float(input(f"You have {money:.2f}$ , how much do you want to bet? "))
   
    if bet <= 0 or bet > money:
        print("Invalid bet! Skipping round.")
        continue
    
    if marble == "green":
        money += bet
        print(
            f"congrats you have won (green) {bet:.2f}$ !\nyour balance : {money:.2f}$ "
        )

    elif marble == "black":
        money += bet * 10
        print(
            f"congrats you have won (black 10X) {bet*10:.2f}$ !\nyour balance : {money:.2f}$ "
        )

    elif marble == "red":
        money -= bet
        print(f"you have lost (red) {bet:.2f}$ !\nyour balance : {money:.2f}$ ")

    elif marble == "white":
        money -= bet * 5
        print(f"you have lost (white 5X) {bet*5:.2f}$ !\nyour balance : {money:.2f}$ ")

    if money < half:
        print("Game over!")
        break
