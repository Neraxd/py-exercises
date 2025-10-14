# 🧠 Exercise: Gym Workout Logger
#
# Goal:
# Write a function `log_workout()` that tracks a user’s exercises and progress.
#
# The function should accept:
# - Positional arguments: user_name, day (e.g., "Monday")
# - Default arguments: duration=60 (minutes of workout)
# - Arbitrary positional arguments (*exercises) — list of exercises done
# - Arbitrary keyword arguments (**stats) — optional stats like calories_burned, heart_rate, notes
#
# Requirements:
# 1. Print the user name and day.
# 2. Print all exercises performed (from *exercises).
# 3. Print the duration of the workout.
# 4. If any stats are provided, print them in a neat format.
# 5. Return a summary string like:
#    "User: Ilia, Day: Monday, Exercises: 3, Duration: 60 min"
#
# 🧪 Mini challenges:
# - Call it with no exercises and only defaults.
# - Call it with several exercises but no stats.
# - Call it with exercises and stats.
# - Try skipping duration using the default while passing stats.
import datetime


def log_workout(user_name, day, *exercises, duration=60, **stats):

    print(f"username:{user_name}\nday:{user_name}\ntime:{datetime.datetime.now()}")
    print("all performed exercises: ")

    if not exercises:
        print("no exercises were done today! ")
    else:
        for e in exercises:
            print(e)

    print(f"total duration: {duration}")

    if stats:
        for num, (skey,svalue) in enumerate(stats.items(), 1):
            print(f"stat number {num} :\n{skey}:{svalue} ")
    else:
        print("no stats were given! ")

    return f"---summary---\nUser: {user_name}, Day: {day}, Exercises: {len(exercises)}, Duration: {duration}min  "


log_workout("ilia","monday")
log_workout("ilia","monday","bench press" , "pushups" , "pullups")
log_workout(
    "ilia",
    "monday",
    "bench press",
    "pushups",
    "pullups",
     stamina=50,
     restlessness=100,
)
