import random

print("Guessing game")

# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

# Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 52-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
counter = 0
number = random.randint(1, 100)

while counter < 10:
    user_input = int(input("guess the number: "))
    if user_input == number:
        print("congrats , you are abseloutly right. ")
        break
    elif user_input > number:
        if counter < 9:
            print("too high")
    elif user_input < number:
        if counter < 9:
            print("too low")
    counter += 1

else:  # this runs if loop finishes without 'break'
    print("Sorry, you lose. The correct number was", number)
