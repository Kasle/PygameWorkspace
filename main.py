import pygame
import Objects
import ObjectManager
import random

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

MANAGER = ObjectManager.Manager()

gameExit = False

MANAGER.addObjects([Objects.PhysicsCircle(gameDisplay, random.randint(0, 800), random.randint(0, 600), random.randint(0, 100), random.randint(0, 100), 10, random.randint(80, 95) / 100.0, 10) for i in range(5)])

print(MANAGER.objects[0].type)

while not gameExit:
    for event in pygame.event.get(): ##Event Handler
       if event.type == pygame.QUIT:
           gameExit = True

    
    gameDisplay.fill(COLOR['BLACK'])

    MANAGER.update()

    pygame.display.update()

    clock.tick(60)

pygame.quit()

quit()
