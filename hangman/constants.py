import pygame
from enum import Enum

resolution = (1280, 720) # Game resolution (don't change since some things are still hardcoded)

# Color constants
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
brown = (181, 101, 29)

# Word center when guessing
wordcenter = (800, 280)

remaining = 6 # Remaining Guesses
usedLetters = []

# Instructions for drawing the hangman
head = [(250, 185), 35, 5]
hangmanComponents = [
    [(50, 400), (200, 400), 10, brown], 
    [(100, 400), (100, 80), 10, brown], 
    [(80, 100), (280, 100), 10, brown], 
    [(150, 100), (100, 150), 10, brown], 
    [(250, 100), (250, 150), 10, brown], 
    [(250, 220), (250, 320), 5, black], 
    [(250, 240), (300, 290), 8, black], 
    [(250, 240), (200, 290), 8, black], 
    [(250, 320), (200, 370), 8, black], 
    [(250, 320), (300, 370), 8, black]
]

# Load images (I made these)
appImg = pygame.image.load("images/icon.png")
guessImg = pygame.image.load("images/guess.png")
menuImg = pygame.image.load("images/menu.png")
winImg = pygame.image.load("images/win.png")
loseImg = pygame.image.load("images/lose.png")

# Keyboard layout
keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"], 
    ["A", "S", "D", "F", "G", "H", "J", "K", "L"], 
    ["Z", "X", "C", "V", "B", "N", "M"]
]
keySpacing = 100 # Horizontal distance between each key
keyCoordinates = [(200, 500), (250, 575), (350, 650)] # Starting coordinates for each row of the keyboard

# Game state enum for better readability
class gameState(Enum):
    START = 1
    GUESS = 2
    LOSE = 3
    WIN = 4

currentState = gameState.START # Initialize to menu

mysteryString = "" # String to be guessed
displayString = None # String to be displayed
displayText = None # Rendered displayString
