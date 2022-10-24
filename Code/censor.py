bannedWords = ["hello"]

def censor(word):
    if word.lower() in bannedWords:
        return "x"*len(word)
    return word

print(" ".join([censor(a) for a in input().split()]))