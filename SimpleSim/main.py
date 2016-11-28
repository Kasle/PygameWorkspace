import pygame
import random
from mapgen import mapManager
import functions as f
import renderer as render

print(pygame.init())  ##(SUCCESS, FAILURE)

mapXY = 800

worldMap = mapManager(mapXY, 1)

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode([mapXY, mapXY], pygame.RESIZABLE)
pygame.display.set_caption("Erador")

##Game Loop

gameExit = False

updateMap = True


while not gameExit:
    for event in pygame.event.get():  ##Event Handler
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print ("H:",worldMap.heightMap[event.pos[0]][event.pos[1]], "| M:",worldMap.moistureMap[event.pos[0]][event.pos[1]], "| T:",worldMap.temperatureMap[event.pos[0]][event.pos[1]], "| B:",worldMap.biomeMap[event.pos[0]][event.pos[1]])

    if updateMap:
        render.colorBiomes(gameDisplay, worldMap, 'h')
        pygame.display.update()
        updateMap = False
    
    clock.tick(30)

pygame.quit()

quit()
