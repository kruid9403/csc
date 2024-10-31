def getTax(total):
    tax = 0.07
    final = round(total * tax)
    print(final)
    return final

def getTip(total):
    tip = 0.18
    final = round(total * tip)
    print(final)
    return final

def mealTotal(total):
    final = total + getTax(total) + getTip(total)
    return final


print(mealTotal(100))
print(mealTotal(135))

def timeCalc(current_time, hours_from_now):
    return (current_time + hours_from_now) % 24

print(timeCalc(13, 12))
print(timeCalc(5, 50))
