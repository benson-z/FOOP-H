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

def reset():
    global displayString, displayText, displayRect, mysteryString, remaining
    remaining = 6
    mysteryString = chooser.choose()
    displayString = "".join(["_" if a != " " else " " for a in mysteryString])
    displayText = pygame.font.Font("RobotoMono-VariableFont_wght.ttf", 72).render(displayString, True, black)
    displayRect = displayText.get_rect()
    displayRect.center = wordcenter

def guess(letter):
    global displayString, displayRect, mysteryString, currentState, displayText, remaining
    newString = ""
    if letter == "":
        return
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
    if y < 450: 
        return ""
    for a in range(len(keyCoordinates)):
        b, c = keyCoordinates[a]
        if abs(y-c) < minimum:
            yIndex = a
            minimum = abs(y-c)
    d, e = keyCoordinates[yIndex]
    xIndex = (x-d+int(keySpacing/2))//keySpacing
    if xIndex >= len(keys[yIndex]) or xIndex < 0:
        return ""
    return keys[yIndex][xIndex]

reset() 

hello = 0

# Main Program
while True:
    if currentState == gameState.GUESS:
        gameDisplay.blit(guessImg, (0, 0))
        drawHangman(remaining)
        gameDisplay.blit(displayText, displayRect)
    if currentState == gameState.LOSE:
        gameDisplay.blit(loseImg, (0, 0))
        displayString = mysteryString.title()
        displayText = pygame.font.Font("RobotoMono-VariableFont_wght.ttf", 60).render(displayString, True, white)
        displayRect = displayText.get_rect()
        displayRect.center = (640, 500)
        gameDisplay.blit(displayText, displayRect)
    if currentState == gameState.WIN:
        gameDisplay.blit(winImg, (0, 0))
    if currentState == gameState.START:
        gameDisplay.blit(menuImg, (0, 0))
        drawHangman(6)
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