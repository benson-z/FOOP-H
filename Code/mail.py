count = 0
count2 = 0

with open("../resources/mail.txt") as f:
    for line in f:
        if line.startswith("From: "):
            count += 1
            if "berkeley.edu" in line:
                count2 += 1

print(count)
print(count2)