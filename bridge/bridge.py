# Benson Zhou - Bridge
# IMPORTANT - This program needs to be run with Python 3.10

import random

# Record the distribution of the card houses. 
distribution = {
    "c": 0, 
    "d": 0,
    "h": 0,
    "s": 0
}
points = 0

# Log of points scored to print to the user
log = []

# Generate a random deck (prevents repeats)
def generate():
    cards = []
    for a in range(13):
        card = random.choice(['c', 'd', 'h', 's']) + random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8' ,'9', '10', 'j', 'q', 'k'])
        if card in cards:
            a -= 1
        else:
            cards.append(card)
    return cards

# Add card to database
def index(card):
    global points, distribution
    distribution[card[0]] += 1
    match card[1]:
        case "a":
            points += 4
            log.append("Ace    +4")
        case "k":
            points += 3
            log.append("King   +3")
        case "q":
            points += 2
            log.append("Queen  +2")
        case "j":
            points += 1
            log.append("Jack   +1")

# Calculate distrubution points
def dist():
    global distribution
    points = 0
    for suit in distribution:
        match distribution[suit]:
            case 0:
                points += 3
            case 1:
                points += 2
            case 2:
                points += 1
    log.append("\nDistrubution Points: +%s" % points)
    return points

# Get cards (generate or input)
if input("\nWhat would you like to do?\n\n(1) Generate a new hand\n(2) Input an existing hand\n\nChoice: ") == '1':
    cards = generate()
    print("\nYour generated deck is: \n" + " ".join(cards))
else:
    cards = input("Input your cards:\n").split()

[index(x) for x in cards]

# New line for spacing
print()

points += dist()

# Print Log
[print(x) for x in log]

# Return total points
print("\nTotal Points:", points)