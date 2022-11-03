import pygame
import math
from enum import Enum

resolution = (1280, 720)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
brown = (181, 101, 29)

wordcenter = (800, 300)

remaining = 6 # Remaining Guesses

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

keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"], 
    ["A", "S", "D", "F", "G", "H", "J", "K", "L"], 
    ["Z", "X", "C", "V", "B", "N", "M"]
]
keySpacing = 100
keyCoordinates = [(200, 500), (250, 575), (350, 650)]

class gameState(Enum):
    START = 1
    GUESS = 2
    LOSE = 3
    WIN = 4

currentState = gameState.START #Change later

mysteryString = ""
displayString = None
displayText = None