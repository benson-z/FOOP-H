# Benson Zhou - Rock Paper Scissors Lizard Spock

import pygame
import math
import random
from enum import Enum

#initial pygame config
pygame.init()

gameDisplay = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Rock Paper Scissors Lizard Spock")
clock = pygame.time.Clock()

# Constants
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
defaultImgSize = (200, 200)

# Load pygame objects
selectionIMG = pygame.image.load("rpsls_select.png")
paper = pygame.transform.scale(pygame.image.load("paper.png"), defaultImgSize)
rock = pygame.transform.scale(pygame.image.load("rock.png"), defaultImgSize)
scissors = pygame.transform.scale(
    pygame.image.load("scissors.png"), defaultImgSize)
lizard = pygame.transform.scale(
    pygame.image.load("lizard.png"), defaultImgSize)
spock = pygame.transform.scale(pygame.image.load("spock.png"), defaultImgSize)
fontObj = pygame.font.SysFont('freesans.tff', 72)
selectionText = pygame.font.SysFont("freesans.ttf", 48).render("Make a Selection", True, black)
selectionRect = selectionText.get_rect()
selectionRect.center = (300, 75)
replayText = pygame.font.SysFont("freesans.ttf", 24).render("Click anywhere to play again", True, black)
replayRect = replayText.get_rect()
replayRect.center = (300, 600)

# Coordinates for selector
lizard_coordinates = (110, 355)
scissors_coordinates = (294, 215)
paper_coordinates = (490, 351)
rock_coordinates = (422, 581)
spock_coordinates = (185, 585)

options = [paper, scissors, lizard, spock, rock]

# Declare a few global variables
selection = 0
mousex = 0
mousey = 0
circlex = 0
circley = 0
computerSelection = 0
statement = None
result = None
resultText = None
resultRect = None
winText = None
winRect = None

# A list of all the possible outcomes for custom messages and maximum efficiency
outcomeList = [
    [("", 0), ("Scissors cuts Paper", -1), ("Lizard eats Paper", -1), ("Paper disproves Spock", 1), ("Paper covers Rock", 1)],
    [("Scissors cuts Paper", 1), ("", 0), ("Scissors decapitates Lizard", 1), ("Spock smashes Scissors", -1), ("Rock crushes Scissors", -1)],
    [("Lizard eats Paper", 1), ("Scissors decapitates Lizard", -1), ("", 0), ("Lizard poisons Spock", 1), ("Rock crushes Lizard", -1)],
    [("Paper disproves Spock", -1), ("Spock smashes Scissors", 1), ("Lizard poisons Spock", -1), ("", 0), ("Spock vaporizes Rock", 1)],
    [("Paper covers Rock", -1), ("Rock crushes Scissors", 1), ("Rock crushes Lizard", 1), ("Spock vaporizes Rock", -1), ("", 0)]
]

# The current state of the program
class programState(Enum):
    SELECT = 2
    PLAY = 3


stage = programState.SELECT

# Calculate the nearest selection based on the angular direction of the mouse cursor from the center
def mousecomp(x, y):
    global lizard_coordinates, scissors_coordinates, paper_coordinates, rock_coordinates, spock_coordinates, selection
    centerx = 300
    centery = 400
    if x == 300:
        if (y < 300):
            return lizard_coordinates
        else:
            return lizard_coordinates
    rotation = math.atan((centery-y)/(x-centerx))
    if y > 400 and x > 300:
        rotation += 2*math.pi
    elif x < 300:
        rotation += math.pi
    rotation = math.degrees(rotation)
    coordinates = [paper_coordinates, scissors_coordinates,
                   lizard_coordinates, spock_coordinates, rock_coordinates]
    selection = int(((rotation+18)/72) % 5)
    return coordinates[selection]

# Simple animation for selection ring
def move_towards(coords):
    x, y = coords
    return (x - (x-circlex)/1.5, y - (y-circley)/1.5)

# Main Program
while True:
    if stage == programState.SELECT:
        gameDisplay.fill(white)
        mousex, mousey = pygame.mouse.get_pos()
        circle_coordinates = mousecomp(mousex, mousey)
        circlex, circley = move_towards(circle_coordinates)
        gameDisplay.blit(selectionIMG, (0, 100))
        gameDisplay.blit(selectionText, selectionRect)
        pygame.draw.circle(gameDisplay, red, (circlex, circley), 90, width=5)
    elif stage == programState.PLAY:
        gameDisplay.fill(white)
        gameDisplay.blit(options[selection], (50, 200))
        gameDisplay.blit(options[computerSelection], (350, 200))
        gameDisplay.blit(resultText, resultRect)
        gameDisplay.blit(winText, winRect)
        gameDisplay.blit(replayText, replayRect)
    # Update pygame
    pygame.display.update()
    clock.tick(60)
    # Events
    for event in pygame.event.get():
        # Normal program exit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Left click actions
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Make selection and calculate game outcome
            if stage == programState.SELECT:
                computerSelection = random.randint(0, 4)
                stage = programState.PLAY
                statement, result = outcomeList[selection][computerSelection]
                resultText = fontObj.render(statement, True, black)
                resultRect = resultText.get_rect()
                resultRect.center = (300, 500)
                if result == 1:
                    winText = fontObj.render("You Win", True, black, green)
                elif result == 0:
                    winText = fontObj.render("Tie", True, black, yellow)
                else:
                    winText = fontObj.render("You Lose", True, black, red)
                winRect = winText.get_rect()
                winRect.center = (300, 100)
                print(statement)
            # Return to selection menu after a game
            else:
                stage = programState.SELECT
