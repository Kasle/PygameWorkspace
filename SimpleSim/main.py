import pygame
import random
from mapgen import mapManager
import functions

print(pygame.init())  ##(SUCCESS, FAILURE)

COLOR = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'YELLOW': (255, 255, 0)
}

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
            print (worldMap.heightMap[event.pos[0]][event.pos[1]])

    if updateMap:
        gameDisplay.fill(COLOR['BLACK'])
        for x in range(len(worldMap.heightMap)):
            for y in range(len(worldMap.heightMap[x])):
                if worldMap.heightMap[x][y] < 0.5: #Water
                    if worldMap.temperatureMap[x][y] < 0:
                        gameDisplay.set_at((x, y), (100, 100, 255))
                    else:
                        gameDisplay.set_at((x, y), (0, 0, 255))
                elif worldMap.heightMap[x][y] >= 0.5 and worldMap.temperatureMap[x][y] < 0 and worldMap.moistureMap[x][y] > 0.1: #Snow
                    gameDisplay.set_at((x, y), (230, 230, 240))
                elif worldMap.heightMap[x][y] < 0.52: #Beach
                    if worldMap.temperatureMap[x][y] < 5:
                        gameDisplay.set_at((x, y), (200, 200, 200))
                    else:
                        gameDisplay.set_at((x, y), (255, 255, 0))
                else:
                    if worldMap.temperatureMap[x][y] > 40:
                        gameDisplay.set_at((x, y), (255, 255, 0))
                    elif worldMap.moistureMap[x][y] > 0.7 and worldMap.temperatureMap[x][y] > 30:
                        gameDisplay.set_at((x, y), (10, 100, 0))
                    elif worldMap.moistureMap[x][y] > 0.3 and worldMap.temperatureMap[x][y] < 10:
                        gameDisplay.set_at((x, y), (0, 120, 50))
                    elif worldMap.moistureMap[x][y] > 0.3 and worldMap.temperatureMap[x][y] > 10:
                        gameDisplay.set_at((x, y), (0, 150, 0))
                    elif worldMap.moistureMap[x][y] < 0.2 and worldMap.temperatureMap[x][y] > 25:
                        gameDisplay.set_at((x, y), (255, 255, 0))
                    elif worldMap.moistureMap[x][y] < 0.2 and worldMap.temperatureMap[x][y] < 25 and worldMap.temperatureMap[x][y] > 15:
                        gameDisplay.set_at((x, y), (200, 200, 100))
                    elif worldMap.heightMap[x][y] > 0.7:
                        gameDisplay.set_at((x, y), 3*[100])
                    elif worldMap.moistureMap[x][y] < 0.2 and worldMap.temperatureMap[x][y] < 15:
                        gameDisplay.set_at((x, y), (100, 130, 100))
                    else:
                        gameDisplay.set_at((x, y), (0, 200, 0))

        pygame.display.update()
        updateMap = False
    
    clock.tick(30)

pygame.quit()

quit()
