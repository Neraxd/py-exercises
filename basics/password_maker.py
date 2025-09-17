#Password Masker 
# #Ask the user for a username and password. 
# Print back the username and the password but with * instead of letters (e.g., mypassword → *********).


username = input("Please enter your username: ")
password = input("Please enter your password: ")

masked_password = "*" * len(password)

print(f"Username: {username}")
print(f"Password: {masked_password}")