# Exercise 9: Calculate the sum and average of the digits present in a string
total = 0
count = 0
def getInt(x):
    global total, count
    try:
        total += int(x)
        count += 1 
    except:
        return
[getInt(a) for a in input("Exercise 9: Calculate the sum and average of the digits present in a string\nInput String: ")]
print("Sum is:", total, "Average is", total/count)

# Exercise 10: Write a program to count occurrences of all characters within a string
occurrences = {}
[occurrences[a] += 1 for a in input()]

# Exercise 16: Removal all characters from a string except integers
output = ""

def isInt(x):
    global output
    try:
        int(x)
        output = output + x
    except:
        return

[isInt(a) for a in input("Exercise 16: Removal all characters from a string except integers\nInput String: ")]

print(output)