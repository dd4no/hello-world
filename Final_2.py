import time
items = []
print("Please enter 10 items.")
Counter = 0
while Counter < 10:
    item = input(">> ").lower()
    items.append(item)
    Counter = Counter + 1
items.sort()
#print(items)
print()
print("Your Items Sorted Alphabetically")
for i in items:
    print(i.capitalize())
    time.sleep(.5)

