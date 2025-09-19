# Create two lists:
# Check if the two lists have the same values (==).
# Check if the two lists are the same object in memory (is and id()).
# Test if "John" is in group1 using in.
# Test if "Brian" is not in group2.
# Create a variable name = "Eric" and check:
# if name is in group1
# if name is group1[0]
# Create two integers a = 256, b = 256. Check a is b.
# Create two integers a = 1000, b = 1000. Check a is b.

group1 = ["Eric", "John", "Terry"]
group2 = ["Eric", "John", "Terry"]
name = "Eric"
a = 256
b = 256
x = 1000
y = 1000
print("checking if the have the same value: ", group1 == group2)
print("checking if they have same memory space: ", group1 is group2)
print("checking if they have same memory space(id): ", id(group1), id(group2))
print("checking if John is in group one: ", "John" in group1)
print("checking if Brian is not in group two: ", "Brian" not in group1)
print("checking if name is in group one: ", name in group1)
print("checking if name is in group one[0]: ", name in group1[0])
print("checking if they have same memory space: ", a is b)
print("checking if they have same memory space: ", x is y)
