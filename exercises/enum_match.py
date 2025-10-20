# Exercise 1: Traffic Light
# --------------------------
# 1. Define an enum `TrafficLight` with values: RED, YELLOW, GREEN.
# 2. Write a function `action(light: TrafficLight)` that uses a match statement to print:
#       - RED -> "Stop"
#       - YELLOW -> "Slow down"
#       - GREEN -> "Go"
# 3. Test your function with each enum value.
from enum import Enum

class TrafficLight(Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"

def action(light:TrafficLight):
    match light:
        case light.RED:
            print("Stop")
        case light.YELLOW:
            print("Slow down")
        case light.GREEN:
            print("GO")


action(TrafficLight.RED)
action(TrafficLight.GREEN)
action(TrafficLight.YELLOW)


