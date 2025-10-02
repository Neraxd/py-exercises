# Bill Splitter 💰

# Ask for total bill and number of friends.

# Show how much each pays.

# Round to 2 decimals.

total_bill = float(input("what's the total? "))
num_of_frens = int(input("how many frens? "))
share = total_bill / num_of_frens

print(f"the total bill is {total_bill} and each should pay {share:.2f}")
