# Benson Zhou - Hangman

#Import constnts file
from constants import *
import chooser

#initial pygame config
pygame.init()
gameDisplay = pygame.display.set_mode(resolution)
pygame.display.set_caption("Hangman")
clock = pygame.time.Clock()

def drawHangman(remaining):
    parts = -4
    for a in hangmanComponents:
        if parts >= remaining:
            break
        pygame.draw.line(gameDisplay, a[3], a[0], a[1], width = a[2])
        parts += 1
    if remaining > 0:
        pygame.draw.circle(gameDisplay, black, head[0], head[1], head[2])

def drawKeys():
    global keys, keySpacing, keyCoordinates
    for row in range(len(keys)):
        x, y = keyCoordinates[row]
        for key in keys[row]:
            keyString = pygame.font.Font("RobotoMono-VariableFont_wght.ttf", 25).render(key, True, black)
            keyRect = keyString.get_rect()
            keyRect.center = (x, y)
            gameDisplay.blit(keyString, keyRect)
            x += keySpacing

def reset():
    global displayString, displayText, displayRect, mysteryString
    mysteryString = chooser.choose()
    displayString = "".join(["_" if a != " " else " " for a in mysteryString])
    displayText = pygame.font.Font("RobotoMono-VariableFont_wght.ttf", 72).render(displayString, True, black)
    displayRect = displayText.get_rect()
    displayRect.center = wordcenter

def guess(letter):
    global displayString, displayRect, mysteryString, currentState, displayText, remaining
    newString = ""
    if letter in displayString:
        print("Letter already used")
        return
    for a in range(len(mysteryString)):
        if mysteryString[a] == letter:
            newString += letter
        else:
            newString += displayString[a]
    if newString == displayString:
        remaining -= 1
        if remaining == 0:
            currentState = gameState.LOSE
    displayString = newString
    displayText = pygame.font.Font("RobotoMono-VariableFont_wght.ttf", 72).render(displayString, True, black)
    displayRect = displayText.get_rect()
    displayRect.center = wordcenter
    if displayString == mysteryString:
        currentState = gameState.WIN

def getKey(coords):
    global keyCoordinates, keys, keySpacing
    x, y = coords
    yIndex = 0
    minimum = 1000000
    for a in range(len(keyCoordinates)):
        b, c = keyCoordinates[a]
        if abs(y-c) < minimum:
            yIndex = a
            minimum = abs(y-c)
    d, e = keyCoordinates[yIndex]
    xIndex = (x-d+int(keySpacing/2))//keySpacing
    return keys[yIndex][xIndex]

reset()

hello = 0

# Main Program
while True:
    if currentState == gameState.GUESS:
        gameDisplay.fill(white)
        drawHangman(remaining)
        gameDisplay.blit(displayText, displayRect)
        drawKeys()
    if currentState == gameState.LOSE:
        gameDisplay.fill(red)
    if currentState == gameState.WIN:
        gameDisplay.fill(green)
    if currentState == gameState.START:
        gameDisplay.fill(red)
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        # Normal program exit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if currentState == gameState.GUESS:
                guess(getKey(pygame.mouse.get_pos()))
            elif currentState == gameState.START:
                currentState = gameState.GUESS
            else:
                reset()
                gameDisplay.fill(white)
                currentState = gameState.START