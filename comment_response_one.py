def a():
    return 1==2
def b():
    return 1==1
def c():
    return 2==2

if a() and b() and c():
    print("All True")
else:
    print("Some False")

if a() or b() or c():
    print("Some True")
else:
    print("All False")

gameOne = {"Vikings": 29, "Lions":31}
gameTwo = {"Ravens":17, "Buccaneers": 10}
gameThree = {"Chargers":3, "Cardinals":7}

scores = []
scores.append(gameOne)
scores.append(gameTwo)
scores.append(gameThree)

print(scores)
