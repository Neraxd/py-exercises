# Create a base class Vehicle with attributes brand and year.
# Create a subclass Car that adds an attribute model.
# Create a Car object and print all its details


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


class Car(Vehicle):
    def __init__(self, model, brand, year):
        super().__init__(brand, year)
        self.model = model


car = Car("bmw", 2012, "E34")

print(f"brand : {car.brand}\nyear : { car.year}\nmodel : {car.model}")
