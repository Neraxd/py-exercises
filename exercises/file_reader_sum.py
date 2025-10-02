# You have a file called numbers.txt that contains:
# 5
# 10
# 15
# 20
# Write a program that:
# Reads all numbers from the file
# Calculates their sum
# Prints the result

with open("/home/ilia/Documents/Python/files/numbers.txt","r") as f:
    sum = 0
    for numbers in f:
        sum += int(numbers)

    print(sum)