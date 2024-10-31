readable = ""
list = ["Steve", "John", "Mike", "Sara", "Sally"]
for i in list:
    readable += i
    if i != list[-1]:
        readable += ", "

print(readable)

def printAPaper(n):
    print("Paper " + str(n + 1))

def getCount(n):
    count = 0
    while count < n:
        printAPaper(count)
        count += 1

getCount(5)