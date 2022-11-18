# Exercise 1

# with open(input()) as f:
#     for line in f:
#         print(line.upper())

# Exercise 2

total = 0
num = 0

with open("../resources/mail.txt") as f:
    for line in f:
        if line.startswith("X-DSPAM-Confidence:"):
            line.strip("\n")
            total += float(line.split()[-1])
            num += 1
            
print("Average spam confidence:", total/num)