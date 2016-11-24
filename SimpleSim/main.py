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

mapXY = 1000

worldMap = mapManager(mapXY, 1)

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
            print ("H:",worldMap.heightMap[event.pos[0]][event.pos[1]], "| M:",worldMap.moistureMap[event.pos[0]][event.pos[1]], "| T:",worldMap.temperatureMap[event.pos[0]][event.pos[1]])

    mode = 'h'
    
    if updateMap:
        gameDisplay.fill(COLOR['BLACK'])
        for x in range(mapXY):
            #print(100*x/float(mapXY))
            for y in range(mapXY):
                if mode == 'h': ##---------------------------
                    
                    if worldMap.heightMap[x][y] < 0.5: ##Water
                        if worldMap.temperatureMap[x][y] < -5: #Glacier
                            gameDisplay.set_at((x, y), (210, 210, 255))
                        elif worldMap.temperatureMap[x][y] < 0: #Frozen Ocean
                            gameDisplay.set_at((x, y), (50, 50, 200))
                        else: #Ocean
                            gameDisplay.set_at((x, y), (0, 0, 200))
                    elif worldMap.temperatureMap[x][y] <= 0 and worldMap.moistureMap[x][y] > 0.1: ##Snow
                        gameDisplay.set_at((x, y), (220, 220, 255))
                    elif worldMap.heightMap[x][y] < 0.5: ##Beach
                        if worldMap.temperatureMap[x][y] < 10: #Gravel Beach
                            gameDisplay.set_at((x, y), (150, 150, 160))
                        else: #Sand Beach
                            gameDisplay.set_at((x, y), (255, 255, 50))  
                    elif worldMap.heightMap[x][y] < 0.8: ##Land
                        if worldMap.temperatureMap[x][y] > 40: #Desert
                            gameDisplay.set_at((x, y), (255, 255, 100))
                        elif worldMap.temperatureMap[x][y] > 30:  #Schrubland
                            if worldMap.moistureMap[x][y] < 0.2:
                                gameDisplay.set_at((x, y), (228, 255, 188))
                            elif worldMap.moistureMap[x][y] < 0.4:
                                gameDisplay.set_at((x, y), (156, 181, 119))
                            elif worldMap.moistureMap[x][y] < 0.6:
                                gameDisplay.set_at((x, y), (202, 214, 124))
                            else:
                                gameDisplay.set_at((x, y), (0, 100, 0))
                        elif worldMap.temperatureMap[x][y] > 20 and worldMap.moistureMap[x][y] < 0.15: #Arid
                            gameDisplay.set_at((x, y), (237, 255, 178))
                        elif worldMap.temperatureMap[x][y] > 10: #Forest
                            if worldMap.moistureMap[x][y] < 0.4:
                                gameDisplay.set_at((x, y), (40, 160, 50))
                            else:
                                gameDisplay.set_at((x, y), (30, 140, 0))
                        elif worldMap.temperatureMap[x][y] > 0: #Tundra
                            if worldMap.moistureMap[x][y] < 0.4:
                                gameDisplay.set_at((x, y), (40, 140, 70))
                            else:
                                gameDisplay.set_at((x, y), (0, 110, 60))
                        else:
                            gameDisplay.set_at((x, y), (0, 255, 255))
                    else: ##Mountains
                        gameDisplay.set_at((x, y), 3*[int(f.fMap(worldMap.heightMap[x][y], 0.8, 1, 70, 120))])
                        
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
