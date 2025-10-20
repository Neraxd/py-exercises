# Exercise 2: Weekday Scheduler
# -----------------------------
# 1. Define an enum `Weekday` with values: MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY.
# 2. Write a function `day_type(day: Weekday)` that uses a match statement to print:
#       - MONDAY to FRIDAY -> "Workday"
#       - SATURDAY, SUNDAY -> "Weekend"
# 3. Test the function with all days of the week.
from enum import Enum


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def day_type(day: Weekday):
    match day:
        case Weekday.SATURDAY | Weekday.SUNDAY:
            print("Weekend!")
        case _:
            print("Workday!")


day_type(Weekday.MONDAY)
day_type(Weekday.TUESDAY)
day_type(Weekday.WEDNESDAY)
day_type(Weekday.THURSDAY)
day_type(Weekday.FRIDAY)
day_type(Weekday.SATURDAY)
day_type(Weekday.SUNDAY)
