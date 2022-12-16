# Exercise 9: Calculate the sum and average of the digits present in a string
str1 = "PYnative29@#8496"

total = 0
count = 0
def getInt(x):
    global total, count
    try:
        total += int(x)
        count += 1 
    except:
        return
[getInt(a) for a in str1]
print("Sum is:", total, "Average is", total/count)

# Exercise 10: Write a program to count occurrences of all characters within a string
str1 = "Apple"
occurrences = {}
def count(char):
    if not char in occurrences:
        occurrences[char] = 0
    occurrences[char] += 1
[count(a) for a in str1]
print(occurrences)

# Exercise 11: Reverse a given string
str1 = "PYnative"
list1 = list(str1)
list1.reverse()
print("".join(list1))

# Exercise 13: Split a string on hyphens

str1 = "Emma-is-a-data-scientist"
[print(x) for x in str1.split("-")]

# Exercise 16: Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'

output = ""

def isInt(x):
    global output
    try:
        int(x)
        output = output + x
    except:
        return

[isInt(a) for a in str1]

print(output)