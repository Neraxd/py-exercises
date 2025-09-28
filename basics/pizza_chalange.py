import platform

#  🍕 Pizza Builder — Challenge Steps
#
# 1. Define a Pizza class that stores:
#    - size, crust type, and a list of toppings
# 2. Add a method to add a new topping
# 3. Add a method to remove a topping if it exists
# 4. Add a method to print pizza details:
#    - size, crust, and all toppings (or “No toppings yet!”)
# 5. Create a pizza object, customize it, and print the summary


class Pizza:
    def __init__(self, size, crust, toppings=[]):
        self.size = size
        self.crust = crust
        self.toppings = toppings

    def add_new_topping(self, topping):
        self.toppings.append(topping)

    def remove_a_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)
        else:
            print("the topic dont exist")

    def printing_details(self):
        print("===== your pizza details =====")
        print(f"pizza size is : {self.size}")
        print(f"crust is : {self.crust}")
        print(f"your toppings are : \n{self.toppings}")


Pizza1 = Pizza(25, "thin")
Pizza1.add_new_topping("tomato sause")
Pizza1.remove_a_topping("pineapple")
Pizza1.printing_details()
print(platform.python_version())