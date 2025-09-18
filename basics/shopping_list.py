# Shopping List
# Create a list with 5 grocery items.
# Print the first and last item.
# Replace the 3rd item with something new.
# Add one more item to the end.
# Print the length of the list.

list = ["tomato" , "pickles" , "mayo" , "ketchup" , "rice"]
first_item = list[0]
last_item = list[-1]

print(f"first item : {first_item} , last item : {last_item} ")

list[2] = "rice cake"
list.append("cheetos") 
# or this => list.insert(-1,"cheetos")

print(f"the length of the list is {len(list)}")
print(f"and  here is the actual list : {list}")

