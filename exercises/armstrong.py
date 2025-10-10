while True:
    number = input("Enter a number: ")
    digits = [int(i) for i in number]

    power = len(digits)
    result = 0

    for x in digits:
        result += x ** power

    if result == int(number):
        print(True)
    else:
        print(False)
