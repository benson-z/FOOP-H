# Benson Zhou - Lucky Sum

sum = 0
unlucky = False

for a in range(3):
    temp = int(input("Enter a number: "))
    if temp == 13:
        unlucky = True
    if not unlucky:
        sum += temp

print(sum)