# 🏁 Pit Stop Timing Optimizer 🔧

# level 1: inputs
total_race_time = float(input('What was the total race time (seconds)? '))
pit_stops_count = int(input('How many pit stops did we have? '))
avg_pit_stop_duration = float(input('What was the average pit stop time (seconds)? '))

# level 2: calculations
total_pit_time = avg_pit_stop_duration * pit_stops_count
percentage_in_pits = (total_pit_time / total_race_time) * 100
percentage_in_pits = round(percentage_in_pits, 2)

# level 3: output
print(f"Total pit stop time: {total_pit_time} seconds")
print(f"Percentage of race time spent in pits: {percentage_in_pits}%")

if percentage_in_pits > 5:
    print("You need a new pit crew. 🛠️")
