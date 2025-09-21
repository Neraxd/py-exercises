# ☕️ Loyalty Points Engine Challenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
# 4. After the loop, call tier_label(total_points)
# 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier

# Purchase history (e.g., 3.75, 7.20, etc.)
purchases = [3.75, 7.20, 10.0, 6.5,10,14.99,117]
total_cost = 0
total_points = 0


def earn_points(price):
    points = int(price) * 3
    return points


def tier_level(total_points):
    if total_points < 100:
        return "bronze"
    elif total_points >= 100 and total_points < 500:
        return "silver"
    elif total_points >= 500:
        return "gold"


for cost in purchases:
    total_points += earn_points(cost)
    total_cost += cost


final_tier = tier_level(total_points)

print(f"====Loyalty summary====")
print(f"total dollors spent: {total_cost}")
print(f"total points : {total_points}")
print(f"final tier: {final_tier}")
