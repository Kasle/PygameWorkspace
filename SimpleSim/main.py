import pygame
import random
import Functions as f
import WorldManager

print(pygame.init())  ##(SUCCESS, FAILURE)

worldSize = 200

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode([worldSize, worldSize], pygame.RESIZABLE)
pygame.display.set_caption("Erador")

#World Setup

gameWorld = WorldManager.World(gameDisplay, worldSize, seed=1, startPopulation=1)

##Game Loop

gameExit = False

while not gameExit:
    for event in pygame.event.get():  ##Event Handler
        if event.type == pygame.QUIT:
            gameExit = True

    gameWorld.tick()

    pygame.display.update()

    clock.tick(2)

pygame.quit()
quit()
