import pygame
import random

class gameObject:
    def __init__(self, size, position, display):
        self.size = size
        self.coords = position
        self.display = display

    def draw(self, globalOffset = (0, 0)):
        pygame.draw.rect(self.display, COLOR['WHITE'], [self.coords[0] + globalOffset[0], self.coords[1] + globalOffset[1], self.size[0], self.size[1]])

print(pygame.init()) ##(SUCCESS, FAILURE)

COLOR = {
    'WHITE' : (255, 255, 255),
    'BLACK' : (0, 0, 0),
    'RED' : (255, 0, 0),
    'GREEN' : (0, 255, 0),
    'BLUE' : (0, 0, 255)
    }

screenSize = [800, 600]

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Slither")

##Game Loop

gameExit = False

leadX = 300
leadY = 300

leadXChange = 0
leadYChange = 0

maxVelocity = 6

mouseLocation = (random.randint(0, 800), random.randint(0, 600))

mouseGlobal = (0, 0)
mousePosition = (0, 0)

globalOffset = (0, 0)
screenOffset = (0, 0)

drag = False
dragInitial = (0, 0)

A = gameObject((10, 10), (0, 0), gameDisplay)

while not gameExit:
    for event in pygame.event.get(): ##Event Handler
        #print(event)
        if event.type == pygame.QUIT:
            gameExit = True
            break
        if event.type == pygame.MOUSEMOTION:
            mousePosition = event.pos
            if not drag:
                mouseGlobal = (mousePosition[0] + globalOffset[0], mousePosition[1] + globalOffset[1])
            else:
                globalOffset = (globalOffset[0] + (mousePosition[0] - dragInitial[0]), globalOffset[1] + (mousePosition[1] - dragInitial[1]))
                dragInitial = mousePosition
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                maxVelocity+=1
            elif event.button == 5:
                maxVelocity-=1
            if event.button == 2:
                drag = True
                dragInitial = mousePosition
        if event.type == pygame.MOUSEBUTTONUP: 
            if event.button == 2:
                drag = False
##            mouseLocation = event.pos
##        if event.type == pygame.MOUSEMOTION:
##            mouseLocation = event.pos
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                leadXChange = -maxVelocity
##            elif event.key == pygame.K_RIGHT:
##                leadXChange = maxVelocity
##            elif event.key == pygame.K_UP:
##                leadYChange = -maxVelocity
##            elif event.key == pygame.K_DOWN:
##                leadYChange = maxVelocity
##
##        if event.type == pygame.KEYUP:
##            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
##                leadXChange = 0
##            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
##                leadYChange = 0
    
    #print(mouseGlobal, globalOffset)
    
    if mouseLocation[0] > leadX:
        if abs(mouseLocation[0] - leadX) > maxVelocity:
            leadXChange = maxVelocity
        else:
            leadXChange = abs(mouseLocation[0] - leadX)
    elif mouseLocation[0] < leadX:
        if abs(mouseLocation[0] - leadX) > maxVelocity:
            leadXChange = -maxVelocity
        else:
            leadXChange = -abs(mouseLocation[0] - leadX)
    else:
        leadXChange = 0

    if mouseLocation[1] > leadY:
        if abs(mouseLocation[1] - leadY) > maxVelocity:
            leadYChange = maxVelocity
        else:
            leadYChange = abs(mouseLocation[1] - leadY)
    elif mouseLocation[1] < leadY:
        if abs(mouseLocation[1] - leadY) > maxVelocity:
            leadYChange = -maxVelocity
        else:
            leadYChange = -abs(mouseLocation[1] - leadY)
    else:
        leadYChange = 0

    if mouseLocation == (leadX, leadY):
        mouseLocation = (random.randint(0, 800), random.randint(0, 600))

    #print (leadX, leadY, leadXChange, leadYChange, mouseLocation[0], mouseLocation[1])
    
    leadX += leadXChange
    leadY += leadYChange
    
    gameDisplay.fill(COLOR['BLACK'])

    pygame.draw.rect(gameDisplay, COLOR['RED'], [mouseLocation[0] + globalOffset[0], mouseLocation[1] + globalOffset[1], 10, 10])
    pygame.draw.rect(gameDisplay, COLOR['WHITE'], [leadX + globalOffset[0], leadY + globalOffset[1], 10, 10]) #(Display, Color, [X, Y, Width, Height])
    A.draw(globalOffset)
    #print(drag)
    
    pygame.display.update()

    clock.tick(60)

pygame.quit()

#quit()
        
