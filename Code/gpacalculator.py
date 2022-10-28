# Benson Zhou - GPA Calculator

conversion = {
    "A": 4,
    "B": 3, 
    "C": 2, 
    "D": 1, 
    "F": 0
}

valid = ["A", "B", "C", "D", "E", "Q"]

grades = ["A"]

while grades[0] != "Q":
    temp = input("Enter Your Grade (Q to exit): ").upper()
    if temp in valid:
        grades.insert(0, temp)

total = 0

for a in range(1, len(grades)-1):
    total += conversion[grades[a]]

print(total/(len(grades)-2))