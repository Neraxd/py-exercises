# Phonebook Manager
# Use a dictionary where keys = names, values = phone numbers.
# Options (loop menu):
# Add contact
# Delete contact
# Search by name
# Show all contacts (sorted alphabetically)
# Quit

phone_book = {}

options_list = """Welcome to the phonbook ! 
          1. add contact
          2. delete contact
          3. search by name
          4. show all contacts
          5. quit \n
          """


def print_optins():
    print(options_list)


print_optins()

while True:
    options = input("please choose an option? ")

    if options == "1":
        name = input("please enter a name :")
        if name in phone_book:
            print_optins()
            print("this contact alredy exists \n")
        else:
            number = input(f"please enter the number for {name} ")
            phone_book.update({name: number})
            print_optins()
            print("contact added successfuly \n")


    elif options == "2":
        name = input("who do you want to delete ? ")
        if name in phone_book:
            deleted_number = phone_book.pop(name)
            print_optins()
            print(f"you have successfully deleted {name} : {deleted_number} contact\n")
        else:
            print_optins()
            print(f"there is no contact by the name of {name}\n")


    elif options == "3":
        name = input("so who are you looking for ? ")
        if name in phone_book:
            search_result = phone_book[name]
            print_optins()
            print(f"this is your search result : {name} : {search_result}")
        else:
            print_optins()
            print(f"there is no contact by the name of {name}\n")


    elif options == "4":
        if phone_book:
            print_optins()
            for num, (name, digits) in enumerate(sorted(phone_book.items()), 1):
                print(f"{num}. {name} \t {digits}")
        else:
            print(f"there is no contact ")
            print_optins()


    elif options == "5":
        choice = input("are you sure y/n ?")
        if choice.lower() == "y":
            break
        elif choice.lower() == "n":
            print_optins()
        else:
            print_optins()
            print("wrong input")


    else:
        print("please chose one of the options in the list!")
        print_optins()
