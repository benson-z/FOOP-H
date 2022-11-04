import random

f = open('words.txt', "r") # Word list from https://skribbliohints.github.io/
wordList = [x.upper().strip("\n") for x in f] # Append each line to a list

def choose():
    return random.choice(wordList)