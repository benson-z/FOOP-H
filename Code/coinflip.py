import random

same = 0
last = -1
flips = 0
total = 0

for x in range(1000):
    while not (same == 2 and last == 0):
        choice = random.randint(0, 1)
        flips += 1
        if choice == last:
            same += 1
        else:
            last = choice
            same = 0
    last = -1
    same = 0
    total += flips
    flips = 0


print(total/1000)