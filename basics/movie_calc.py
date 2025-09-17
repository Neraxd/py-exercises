# Movie Time Calculator 🎬

# Ask for total minutes watched.

# Print it as hours + minutes (e.g., 134 minutes → 2 hours 14 minutes).

total_watched = float(input("Enter the total: "))
hours = int(total_watched // 60)
minutes = total_watched % 60

print(f"you have watched movies for {hours} hours and {minutes} minutes")
