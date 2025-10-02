# Write a function divide(a, b) that:

# Raises a ValueError if b == 0 with message "Division by zero not allowed!"

# Otherwise, returns the result of a / b.
# Test it with divide(10, 2) and divide(5, 0).

def divide(a,b):
    try:
        result = a / b
        if b == 0 :
            raise ZeroDivisionError
    except ZeroDivisionError:
        print("Division by zero not allowed!")
    else : 
        return result
    


print(divide(10,2))
divide(5, 0)
