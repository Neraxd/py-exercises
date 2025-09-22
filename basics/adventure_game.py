# It’s...not really an adventure game...#Ver 1.0
# Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
# The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
# ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought
# (typed)
# Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
freelancers = {
    "name": "freelancing Shop",
    "brian": 70,
    "black knight": 20,
    "biccus diccus": 100,
    "grim reaper": 500,
    "minstrel": -15,
}
antiques = {
    "name": "Antique Shop",
    "french castle": 400,
    "wooden grail": 3,
    "scythe": 150,
    "catapult": 75,
    "german joke": 5,
}
pet_shop = {"name": "Pet Shop", "blue parrot": 10, "white rabbit": 5, "newt": 2}


cart = {}
purse = 1000
total_cost = 0

inventory = {**freelancers,**antiques,**pet_shop}
print(inventory)

for shop in (freelancers, antiques, pet_shop):
    print(f"welcome to the {shop["name"]} ")
    catalog = ""

    for key, value in shop.items():
        if key == "name":
            continue
        else:
            catalog += f"{key} : {value}\n"
    item = input(f"what do you want?\n{catalog} ").lower()

    if item == "exit":
        continue
    if item not in shop:
        print("That item doesn’t exist. Moving to next store.")
        continue
    cart.update({item: shop.pop(item)})
    
    item = ", ".join(list(cart.keys()))


total_cost = sum(cart.values())
purse = purse - total_cost

if len(cart.values()) == 0:
    print("you bought nothing , we are all gonna die")
else :
    print(f"\nYou purchased: {', '.join(cart.keys())}. Today it is all free!")

print(f"Total cost: {total_cost} \t Gold left: {purse}")
inventory = {**freelancers, **antiques, **pet_shop}
inventory.pop("name")
print(inventory)
