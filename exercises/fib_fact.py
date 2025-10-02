def fib(n):
    a = 0
    b = 1
    c = 0
    print(a)
    print(b)
    for x in range(n):
        c = a + b
        print(c)
        a = b
        b = c


def fact(n):

    for i in range(n):
        number = int(input(f"enter the number {i+1} : "))
        fact = 1
        for x in range(1, number + 1):
            fact *= x
        print(f"fact of {number} is : {fact}")


while True:

    print(
        """
    1. fib
    2. fact 
    3. exit
    """
    )

    option = input("which one do you want ? \n")

    if option == "1":
        item_count = int(input("how many items? "))
        fib(item_count)
    elif option == "2":
        number_count = int(input("how many numbers do you have? "))
        fact(number_count)
    elif option == "3":
        break
