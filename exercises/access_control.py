# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.

revoked_badge_numbers = {33, 22, 14, 13, 67}
approved = []
denied = []

while True:
    name = input("what's your name? ")
    if name == "done":
        break

    badge_number = int(input("what's your badge number? "))

    if badge_number in revoked_badge_numbers:
        print("access denied")
        denied.append(name)
    else:
        print("access granted")
        approved.append(name)


print("===== Access summary =====")
print("===== denied users: ")

for num, user in enumerate(sorted(denied), 1):
    print(f"{num}. {user}")

print("===== approved users: ")

for num, user in enumerate(sorted(approved), 1):
    print(f"{num}. {user}")

print(f"approved total number : {len(approved)}")
print(f"denied total number : {len(denied)}")
