def mealTotal(total):
    tax = 0.07
    tip = 0.18
    total = total + (total * tax) + (total * tip)
    return total

print(mealTotal(100))
print(mealTotal(135))

def timeCalc(current_time, hours_from_now):
    return (current_time + hours_from_now) % 24

print(timeCalc(13, 12))
print(timeCalc(5, 50))
