import pygame
import random
from mapgen import mapManager
import functions as f

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

worldMap = mapManager(mapXY, 1000)

minTemperature = min([min(i) for i in worldMap.temperatureMap ])
maxTemperature = max([max(i) for i in worldMap.temperatureMap ])
avgTemperature = ( minTemperature + maxTemperature ) / 2.0

print(sum([ sum(i) for i in worldMap.temperatureMap]) / float(mapXY**2))

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

    mode = 'h'
    
    if updateMap:
        gameDisplay.fill(COLOR['BLACK'])
        for x in range(mapXY):
            #print(100*x/float(mapXY))
            for y in range(mapXY):
                if mode == 'h': ##---------------------------

                    if worldMap.biomeMap[x][y] == 'water':
                        gameDisplay.set_at((x, y), (0, 0, 200))
                    elif worldMap.biomeMap[x][y] == 'frozenWater':
                        gameDisplay.set_at((x, y), (100, 100, 200))
                    elif worldMap.biomeMap[x][y] == 'glacier':
                        gameDisplay.set_at((x, y), (255, 255, 255))
                    elif worldMap.biomeMap[x][y] == 'snow':
                        gameDisplay.set_at((x, y), (255, 255, 255))
                    elif worldMap.biomeMap[x][y] == 'snowyMountain':
                        gameDisplay.set_at((x, y), (255, 255, 255))
                    elif worldMap.biomeMap[x][y] == 'mountain':
                        gameDisplay.set_at((x, y), (120, 120, 120))
                    elif worldMap.biomeMap[x][y] == 'permafrost':
                        gameDisplay.set_at((x, y), (255, 255, 255))
                    elif worldMap.biomeMap[x][y] == 'tundra':
                        gameDisplay.set_at((x, y), (150, 150, 200))
                    elif worldMap.biomeMap[x][y] == 'alpineTundra':
                        gameDisplay.set_at((x, y), (100, 200, 150))
                    elif worldMap.biomeMap[x][y] == 'taiga':
                        gameDisplay.set_at((x, y), (0, 150, 100))
                    elif worldMap.biomeMap[x][y] == 'boreal':
                        gameDisplay.set_at((x, y), (0, 170, 0))
                    elif worldMap.biomeMap[x][y] == 'grassPlains':
                        gameDisplay.set_at((x, y), (80, 180, 20))
                    elif worldMap.biomeMap[x][y] == 'savanna':
                        gameDisplay.set_at((x, y), (90, 170, 0))
                    elif worldMap.biomeMap[x][y] == 'wildPlains':
                        gameDisplay.set_at((x, y), (100, 170, 0))
                    elif worldMap.biomeMap[x][y] == 'barrenPlains':
                        gameDisplay.set_at((x, y), (120, 190, 50))
                    elif worldMap.biomeMap[x][y] == 'jungle':
                        gameDisplay.set_at((x, y), (30, 100, 0))
                    elif worldMap.biomeMap[x][y] == 'desert':
                        gameDisplay.set_at((x, y), (255, 255, 150))
                    else:
                        gameDisplay.set_at((x, y), (255, 0, 255))
                    
                elif mode == 'm': ##-------------------------
                    
                    gameDisplay.set_at((x, y), 3*[f.fMap(worldMap.moistureMap[x][y], 0, 1, 0, 255)])
                    
                elif mode == 't': ##-------------------------
                    
                    if worldMap.temperatureMap[x][y] < avgTemperature:
                        gameDisplay.set_at((x, y), (int(f.fMap(worldMap.temperatureMap[x][y], minTemperature, avgTemperature, 0, 255)),int(f.fMap(worldMap.temperatureMap[x][y], minTemperature, avgTemperature, 0, 255)), 255))
                    else:
                        gameDisplay.set_at((x, y), (255, int(f.fMap(worldMap.temperatureMap[x][y], avgTemperature, maxTemperature, 255, 0)), int(f.fMap(worldMap.temperatureMap[x][y], avgTemperature, maxTemperature, 255, 0))))

        pygame.display.update()
        updateMap = False
    
    clock.tick(30)

pygame.quit()

quit()
