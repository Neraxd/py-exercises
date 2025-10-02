# Problem 1:
# Create a base class Animal with method speak().
# Create subclasses Dog and Cat that override speak() to return "Woof!" and "Meow!".
# Test the classes.


class Animal:
    def speak(self):
        return None  # or pass


class Cat(Animal):
    def speak(self):
        return "meow"


class Dog(Animal):
    def speak(self):
        return "woof"


dog = Dog()
cat = Cat()
animal = Animal()


print(dog.speak(), cat.speak(), animal.speak())
