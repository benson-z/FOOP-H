import random

f = open('words.txt', "r")
wordList = [x.upper().strip("\n") for x in f]

print(wordList)

def choose():
    return random.choice(wordList)