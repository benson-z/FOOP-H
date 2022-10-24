a = int(input("First num:\n"))
b = int(input("Second num:\n"))

sum = 0

for a in range(min(a, b), max(a, b)+1):
    sum += a

print(sum)