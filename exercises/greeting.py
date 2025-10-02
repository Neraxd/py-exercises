# Write a function greet(name, age) that:
# Takes a name and age as input.
# Returns a string:
# "Hello Eric, you are 18 years old!"
# ✅ Call it with positional arguments and again with named arguments.


def gretting(name, age):
    return f"Hello {name}, you are {age} years old!"


result = gretting("Eric", 18)
result_named_notation = gretting(age=18, name="Eric")

print(f"{result}\n{result_named_notation}")
