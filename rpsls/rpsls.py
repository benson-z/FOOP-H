# Benson Zhou - Rock Paper Scissors Lizard Spock

import pygame
import math
import random
from enum import Enum

pygame.init()

gameDisplay = pygame.display.set_mode((600,700))
pygame.display.set_caption("Rock Paper Scissors Lizard Spock")
clock = pygame.time.Clock()

# Constants
white = (255, 255, 255)
red = (255, 0, 0)
defaultImgSize = (200, 200)
selectionIMG = pygame.image.load("rpsls_select.png")
paper = pygame.transform.scale(pygame.image.load("paper.png"), defaultImgSize)
rock = pygame.transform.scale(pygame.image.load("rock.png"), defaultImgSize)
scissors = pygame.transform.scale(pygame.image.load("scissors.png"), defaultImgSize)
lizard = pygame.transform.scale(pygame.image.load("lizard.png"), defaultImgSize)
spock = pygame.transform.scale(pygame.image.load("spock.png"), defaultImgSize)
lizard_coordinates = (110, 355)
scissors_coordinates = (294, 215)
paper_coordinates = (490, 351)
rock_coordinates = (419, 581)
spock_coordinates = (183, 581)
options = [paper, scissors, lizard, spock, rock]
selection = 0
mousex = 0
mousey = 0
circlex = 0
circley = 0
computerSelection = 0
statement = ""
result = ""

outcomeList = [
	[("Tie", 0), ("Scissors cuts Paper", 1), ("Lizard eats Paper", -1), ("Paper disproves Spock", 1), ("Paper covers Rock", 1)], 
	[], 
	[],
	[()], 
	[("Paper covers Rock", -1), ("Rock crushes Scissors", 1), ("Rock crushes Lizard", 1), ("Spock vaporizes Rock", -1), ("Tie", 0)]
]

class programState(Enum):
	WIN = 1
	LOSE = -1
	TIE = 0
	SELECT = 2
	PLAY = 3

stage = programState.SELECT

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
	if y > 400 and x>300:
		rotation += 2*math.pi
	elif x<300:
		rotation += math.pi
	rotation = math.degrees(rotation)
	coordinates = [paper_coordinates, scissors_coordinates, lizard_coordinates, spock_coordinates, rock_coordinates]
	selection = int(((rotation+18)/72)%5)
	return coordinates[selection]

def move_towards(coords):
	x, y = coords
	return (x - (x-circlex)/1.5, y - (y-circley)/1.5)

while True:
	if stage == programState.SELECT:
		gameDisplay.fill(white)
		mousex, mousey = pygame.mouse.get_pos()
		circle_coordinates = mousecomp(mousex, mousey)
		circlex, circley = move_towards(circle_coordinates)
		gameDisplay.blit(selectionIMG, (0, 100))
		pygame.draw.circle(gameDisplay, red, (circlex, circley), 90, width=5)
	elif stage == programState.PLAY:
		gameDisplay.fill(white)
		gameDisplay.blit(options[selection], (50, 200))
		gameDisplay.blit(options[computerSelection], (350, 200))
	pygame.display.update()
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			if stage == programState.SELECT:
				computerSelection = random.randint(0, 4)
				stage = programState.PLAY
				statement, result = outcomeList[selection][computerSelection]
				print(statement)