# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."

phone_number = input("Enter a US phone number")

phone_number = phone_number.strip()

for ch in ["-", "(", ")", "."]:
    phone_number = phone_number.replace(ch, " ")

phone_number = phone_number.split()
phone_number = "".join(phone_number)

if len(phone_number) == 10:
    phone_number = f"({phone_number[0:3]}) {phone_number[3:6]}-{phone_number[6:]}"
    print(phone_number)

else:
    print("Please enter exactly 10 digits.")


# ✅ Test it out!
#
#  - 123-456-7890
#  - (123)4567890
#  - 123. 456 . 7890
#  -    123 456 7890
#  - 1234567890
