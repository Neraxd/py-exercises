# 🐾 Dog Bus Tracker — Challenge Steps
#
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time
#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
#
# 3. Add one new pet if there’s room on the bus.
#    - Use MAX_SEATS to limit capacity.
#    - Dynamically assign the next seat number.
#    - Print the updated roster showing all pets after pickup.
#
# 4. Ask which pet leaves early.
#    - Remove that pet from the bus.
#    - Print a message saying they’ve headed home.
#
# 5. Print a final roster listing the remaining pets and their dropoff times.
MAX_SEATS = 4

passangers = {
    1: {"name": "alec", "breed": "husky", "pickup time": 9, "drop off time": 13},
    2: {"name": "nemo", "breed": "bulldog", "pickup time": 10, "drop off time": 13},
    3: {
        "name": "sardin",
        "breed": "aregentino doggo",
        "pickup time": 10,
        "drop off time": 13,
    },
}


def rooster(key):

    print(f"==== seat {key} =====")
    if key == "final":
        print(f"number of passangers: {len(passangers.keys())}")
    for seat, info in passangers.items():
        print(f"seat number : {seat} ")
        print(f"name : {info["name"]} ")
        print(f"pickup time : {info["pickup time"]} ")
        print("==================================")


def adding(passangers):
    if len(passangers.keys()) < MAX_SEATS:
        for item in range(MAX_SEATS - len(passangers.keys())):
            print(f"the bus has {item + 1} empty seats")
            new_passengar = input("name ?  ")
            new_breed = input("what breed?  ")
            new_pickup = int(input("pickup time? "))
            new_dropoff = int(input("dropoff time? "))
            passangers[len(passangers.keys()) + 1] = {
                "name": new_passengar,
                "breed": new_breed,
                "pickup time": new_pickup,
                "drop off time": new_dropoff,
            }
    else:
        print("no available seats")
    rooster("updated")


def leaving():
    pet_name = input("who wants to leave? ")
    for key, value in passangers.items():

        if pet_name == value["name"]:
            passangers.pop(key)
            print(f"{pet_name} has left the boss and is heading home")
            break



rooster("starting")
adding(passangers)
leaving()
rooster("final")
