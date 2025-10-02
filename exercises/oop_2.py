# Create a class Circle with attribute radius.

# Add a method area() that returns the circle’s area.

# Create a circle object with radius 5 and print its area.


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * (self.radius**2)
        return area


circle1 = Circle(5)
print(circle1.area())
