import pygame
import functions as f

COLOR = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'YELLOW': (255, 255, 0)
}

def colorBiomes(display, worldMap, genType):
    mode = genType
    display.fill(COLOR['BLACK'])
    for x in range(worldMap.getSize()):
        #print(100*x/float(worldMap.getSize()))
        for y in range(worldMap.getSize()):
            if mode == 'h': ##---------------------------

                if worldMap.biomeMap[x][y] == 'lake':
                    display.set_at((x, y), (0, 0, 200))
                elif worldMap.biomeMap[x][y] == 'river':
                    display.set_at((x, y), (40, 40, 220))
                elif worldMap.biomeMap[x][y] == 'riverLake':
                    display.set_at((x, y), (40, 40, 220))
                elif worldMap.biomeMap[x][y] == 'frozenLake':
                    display.set_at((x, y), (100, 100, 200))
                elif worldMap.biomeMap[x][y] == 'frozenOcean':
                    display.set_at((x, y), (80, 80, 200))
                elif worldMap.biomeMap[x][y] == 'ocean':
                    display.set_at((x, y), (0, 0, 180))
                elif worldMap.biomeMap[x][y] == 'glacier':
                    display.set_at((x, y), (230, 230, 255))
                elif worldMap.biomeMap[x][y] == 'snow':
                    display.set_at((x, y), (255, 255, 255))
                elif worldMap.biomeMap[x][y] == 'snowyMountain':
                    display.set_at((x, y), (220, 220, 230))
                elif worldMap.biomeMap[x][y] == 'mountain':
                    display.set_at((x, y), 3*[f.fMap(worldMap.heightMap[x][y], 0.75, 1, 80, 120)])
                elif worldMap.biomeMap[x][y] == 'permafrost':
                    display.set_at((x, y), (255, 255, 255))
                elif worldMap.biomeMap[x][y] == 'tundra':
                    display.set_at((x, y), (150, 150, 160))
                elif worldMap.biomeMap[x][y] == 'alpineTundra':
                    display.set_at((x, y), (100, 140, 110))
                elif worldMap.biomeMap[x][y] == 'taiga':
                    display.set_at((x, y), (0, 130, 60))
                elif worldMap.biomeMap[x][y] == 'snowyTaiga':
                    display.set_at((x, y), (255, 255, 255))
                elif worldMap.biomeMap[x][y] == 'boreal':
                    display.set_at((x, y), (0, 150, 0))
                elif worldMap.biomeMap[x][y] == 'temperate':
                    display.set_at((x, y), (0, 170, 0))
                elif worldMap.biomeMap[x][y] == 'grassPlains':
                    display.set_at((x, y), (80, 180, 20))
                elif worldMap.biomeMap[x][y] == 'savanna':
                    display.set_at((x, y), (90, 170, 0))
                elif worldMap.biomeMap[x][y] == 'wildPlains':
                    display.set_at((x, y), (100, 170, 0))
                elif worldMap.biomeMap[x][y] == 'barrenPlains':
                    display.set_at((x, y), (120, 190, 50))
                elif worldMap.biomeMap[x][y] == 'jungle':
                    display.set_at((x, y), (30, 100, 0))
                elif worldMap.biomeMap[x][y] == 'desert':
                    display.set_at((x, y), (255, 255, 150))
                else:
                    display.set_at((x, y), (255, 0, 255))
                
            elif mode == 'm': ##-------------------------
                
                display.set_at((x, y), 3*[int(f.fMap(worldMap.moistureMap[x][y], 0, 1, 0, 255))])

            elif mode == 'r': ##-------------------------
                
                display.set_at((x, y), 3*[int(f.fMap(worldMap.resourceMap[x][y], 0, 1, 0, 255))])
                
            elif mode == 't': ##-------------------------
                
                if worldMap.temperatureMap[x][y] < avgTemperature:
                    display.set_at((x, y), (int(f.fMap(worldMap.temperatureMap[x][y], minTemperature, avgTemperature, 0, 255)),int(f.fMap(worldMap.temperatureMap[x][y], minTemperature, avgTemperature, 0, 255)), 255))
                else:
                    display.set_at((x, y), (255, int(f.fMap(worldMap.temperatureMap[x][y], avgTemperature, maxTemperature, 255, 0)), int(f.fMap(worldMap.temperatureMap[x][y], avgTemperature, maxTemperature, 255, 0))))
