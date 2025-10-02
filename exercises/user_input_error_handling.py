# Write a program that asks the user for a number.
# If the input is not an integer, catch the exception and print: "Please enter a valid number!".
# expand the problem with a while loop

while True:
    try:
        number = int(input("Please enter a number : "))

    except ValueError:
        print("user input should be an integer")
        continue
    else:
        print(f"your number was {number} , thanks")
        break
