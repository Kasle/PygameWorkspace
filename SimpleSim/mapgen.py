import noise
import random
import functions as f
from time import sleep

class mapManager:

    def __init__(self, size, seed):
        
        self.seed = seed

        random.seed(seed)
        
        self.heightSeed = random.randint(0, 100000000)
        self.moistureSeed = random.randint(0, 100000000)
        self.temperatureSeed = random.randint(0, 100000000)
        self.resourceSeed = random.randint(0, 100000000)
        
        self.mapSize = size
        self.heightMap = []
        self.temperatureMap = []
        self.moistureMap = []
        self.resourceMap = []
        self.biomeMap = []
        self.foodMap = []
        self.generateMaps()


    def generateMaps(self):
        print("Generating Height Map...")
        self.heightMap = self.generateHeightMap()
        print("Generating Moisture Map...")
        self.moistureMap = self.generateMoistureMap()
        print("Generating Temperature Map...")
        self.temperatureMap = self.generateTemperatureMap()
        print("Generating Resource Map...")
        self.resourceMap = self.generateResourceMap()
        print("Generating Biome Map...")
        self.biomeMap = self.generateBiomeMap()
        print("Generating Oceans...")
        self.oceanMap()
        print("Generating Rivers...")
        self.riverMap()
        print("Generating Terrain Bounty...")
        self.generateFoodMap()
        print("Generation Complete.")

    
    def generateHeightMap(self):
        
        tempMap = f.generateNoiseMap(self.heightSeed, self.mapSize, 0.008, 0.2, 1, 10, 0.75, 1.5) #Map Values
        
        for x in range(self.mapSize):
            for y in range(self.mapSize):
                absRange = min(self.mapSize/2.0, ((x-self.mapSize/2)**2 + (y-self.mapSize/2)**2)**0.5)
                heightMultiplier = - ( absRange / (self.mapSize/2.0) )**10 + 1
                tempMap[x][y] *= heightMultiplier
        return tempMap


    def generateMoistureMap(self):
        
        tempMap = f.generateNoiseMap(self.moistureSeed, self.mapSize, 0.008, 0, 1, 7, 0.4, 1.5)
        
        for x in range(self.mapSize):
            for y in range(self.mapSize):
                tempMap[x][y] = 0.6*tempMap[x][y] + 0.4*f.fMap(self.heightMap[x][y], 0, 1, 1, 0)
        return tempMap


    def generateTemperatureMap(self):
        
        tempMap = f.generateNoiseMap(self.moistureSeed, self.mapSize, 0.01, -5, 5, 10, 0.8, 1.5)
        
        for x in range(self.mapSize):
            for y in range(self.mapSize):
                tempMap[x][y] = tempMap[x][y] + f.fMap(y, 0, self.mapSize, -10, 40) + 0.7*f.fMap(self.moistureMap[x][y], 0, 1, 0, 10) + min(0, f.fMap(self.heightMap[x][y], 0, 1, 50, -25))
            
        return tempMap


    def generateResourceMap(self):
        
        tempMap = f.generateNoiseMap(self.moistureSeed, self.mapSize, 0.05, 0, 1, 5, 0.4, 1.5)
        
        for x in range(self.mapSize):
            for y in range(self.mapSize):
                tempMap[x][y] = tempMap[x][y] * (0.5*f.fMap(max(0, min(self.temperatureMap[x][y], 20)), 0, 20, 0, 1) + 0.5*f.fMap(max(20, min(self.temperatureMap[x][y], 30)), 20, 30, 1, 0))
            
        return tempMap


    def generateBiomeMap(self):
        tempMap = [['none' for i in range(self.mapSize)] for j in range(self.mapSize)]

        for x in range(self.mapSize):
            for y in range(self.mapSize):
                
                if self.heightMap[x][y] >= 0.75:
                    if self.temperatureMap[x][y] < 0:
                        tempMap[x][y] = 'snowyMountain'
                    else:
                        tempMap[x][y] = 'mountain'
                elif self.temperatureMap[x][y] < -5: ##Permafrost
                    if self.heightMap[x][y] < 0.5:
                        tempMap[x][y] = 'glacier'
                    else:
                        tempMap[x][y] = 'permafrost'
                elif self.temperatureMap[x][y] < 0:
                    if self.heightMap[x][y] < 0.5:
                        tempMap[x][y] = 'frozenLake'
                    elif self.moistureMap[x][y] < 0.7:
                        tempMap[x][y] = 'snowyTaiga'
                    else:
                        tempMap[x][y] = 'snow'
                elif self.heightMap[x][y] < 0.5:
                    tempMap[x][y] = 'lake'
                elif self.temperatureMap[x][y] < 5:
                    if self.moistureMap[x][y] < 0.5:
                        tempMap[x][y] = 'tundra'
                    elif self.moistureMap[x][y] < 0.6:
                        tempMap[x][y] = 'alpineTundra'
                    else:
                        tempMap[x][y] = 'taiga'
                elif self.temperatureMap[x][y] < 10:
                    if self.moistureMap[x][y] < 0.4:
                        tempMap[x][y] = 'alpineTundra'
                    else:
                        tempMap[x][y] = 'taiga'
                elif self.temperatureMap[x][y] < 15:
                    if self.moistureMap[x][y] < 0.3:
                        tempMap[x][y] = 'barrenPlains'
                    else:
                        tempMap[x][y] = 'boreal'
                elif self.temperatureMap[x][y] < 25:
                    if self.moistureMap[x][y] < 0.2:
                        tempMap[x][y] = 'barrenPlains'
                    elif self.moistureMap[x][y] < 0.4:
                        tempMap[x][y] = 'grassPlains'
                    else:
                        tempMap[x][y] = 'temperate'
                elif self.temperatureMap[x][y] < 27:
                    if self.moistureMap[x][y] < 0.3:
                        tempMap[x][y] = 'barrenPlains'
                    else:
                        tempMap[x][y] = 'savanna'
                elif self.temperatureMap[x][y] < 30:
                    if self.moistureMap[x][y] < 0.5:
                        tempMap[x][y] = 'wildPlains'
                    else:
                        tempMap[x][y] = 'temperate'
                elif self.temperatureMap[x][y] < 35:
                    if self.moistureMap[x][y] < 0.4:
                        tempMap[x][y] = 'wildPlains'
                    else:
                        tempMap[x][y] = 'jungle'
                else:
                    if self.moistureMap[x][y] < 0.4:
                        tempMap[x][y] = 'desert'
                    elif self.moistureMap[x][y] < 0.5:
                        tempMap[x][y] = 'wildPlains'
                    else:
                        tempMap[x][y] = 'jungle'
                              
        return tempMap

    def oceanMap(self):
        checkPoints = [[0, 0]]
        checked = [['' for i in range(self.mapSize)] for j in range(self.mapSize)]
        while True:
            if not checkPoints:
                break
            
            cp = checkPoints.pop(0)
            
            if self.biomeMap[cp[0]][cp[1]] == 'frozenLake':
                self.biomeMap[cp[0]][cp[1]] = 'frozenOcean'
            elif self.biomeMap[cp[0]][cp[1]] == 'lake':
                self.biomeMap[cp[0]][cp[1]] = 'ocean'

            checked[cp[0]][cp[1]] = 'c'
            
            for xD in [-1, 0, 1]:
                for yD in [-1, 0, 1]:
                    
                    if cp[0] + xD >= 0 and cp[0] + xD <= self.mapSize-1:
                        if cp[1] + yD >= 0 and cp[1] + yD <= self.mapSize-1:
                            if not checked[cp[0]+xD][cp[1]+yD] == 'c':
                                if self.biomeMap[cp[0]+xD][cp[1]+yD] == 'glacier' or self.biomeMap[cp[0]+xD][cp[1]+yD] == 'frozenLake' or self.biomeMap[cp[0]+xD][cp[1]+yD] == 'lake':
                                    checkPoints.append([cp[0]+xD, cp[1]+yD])
                                    checked[cp[0]+xD][cp[1]+yD] = 'c'

    def riverMap(self):
        riverSeeds = []

        for x in range(self.mapSize):
            for y in range(self.mapSize):
                if self.biomeMap[x][y] == 'mountain':
                    if random.random() < 0.001:
                        riverSeeds.append([x, y])

        ind = 0
        
        while True:
            if not riverSeeds:
                break

            low = 1
            pos = []
            isComplete = False
            
            for xD in [-1, 0, 1]:
                for yD in [-1, 0, 1]:
                    if isComplete:
                        break
                    
                    if not (xD == 0 and yD == 0):
                        if self.biomeMap[riverSeeds[0][0] + xD][riverSeeds[0][1] + yD] == 'river' or self.biomeMap[riverSeeds[0][0] + xD][riverSeeds[0][1] + yD] == 'riverLake':
                            continue
                        if self.heightMap[riverSeeds[0][0] + xD][riverSeeds[0][1] + yD] < 0.5:
                            isComplete = True
                            continue
                        if self.heightMap[riverSeeds[0][0] + xD][riverSeeds[0][1] + yD] <= low:
                            low = self.heightMap[riverSeeds[0][0] + xD][riverSeeds[0][1] + yD]
                            pos = [riverSeeds[0][0] + xD,riverSeeds[0][1] + yD]

            if self.heightMap[riverSeeds[0][0]][riverSeeds[0][1]] < low:
                self.biomeMap[riverSeeds[0][0]][riverSeeds[0][1]] = 'riverLake'
            else:
                self.biomeMap[riverSeeds[0][0]][riverSeeds[0][1]] = 'river'

            if pos == []:
                isComplete = True

            riverSeeds.pop(0)

            if isComplete:
                continue
            
            riverSeeds.append(pos)

    def generateFoodMap(self):
        tempMap = [[0 for i in range(self.mapSize)] for j in range(self.mapSize)]

        for x in range(self.mapSize):
            for y in range(self.mapSize):
                foodCount = 0

                if self.biomeMap[x][y] == 'lake':
                    foodCount += 1
                elif self.biomeMap[x][y] == 'river':
                    foodCount += 1
                elif self.biomeMap[x][y] == 'riverLake':
                    foodCount += 1
                elif self.biomeMap[x][y] == 'forzenLake':
                    foodCount += 0.5
                elif self.biomeMap[x][y] == 'frozenOcean':
                    foodCount += 0.25
                elif self.biomeMap[x][y] == 'ocean':
                    foodCount += 1
                elif self.biomeMap[x][y] == 'snow':
                    foodCount += 0.1
                elif self.biomeMap[x][y] == 'mountain':
                    foodCount += 0.2
                elif self.biomeMap[x][y] == 'tundra':
                    foodCount += 0.25
                elif self.biomeMap[x][y] == 'alpineTundra':
                    foodCount += 0.5
                elif self.biomeMap[x][y] == 'taiga':
                    foodCount += 0.75
                elif self.biomeMap[x][y] == 'snowyTaiga':
                    foodCount += 0.5
                elif self.biomeMap[x][y] == 'boreal':
                    foodCount += 1
                elif self.biomeMap[x][y] == 'temperate':
                    foodCount += 1.5
                elif self.biomeMap[x][y] == 'grassPlains':
                    foodCount += 2
                elif self.biomeMap[x][y] == 'savanna':
                    foodCount += 0.75
                elif self.biomeMap[x][y] == 'wildPlains':
                    foodCount += 0.7
                elif self.biomeMap[x][y] == 'barrenPlains':
                    foodCount += 0.6
                elif self.biomeMap[x][y] == 'jungle':
                    foodCount += 1
                elif self.biomeMap[x][y] == 'desert':
                    foodCount += 0.1
    
    def getSeed(self):
        return self.seed


    def getSize(self):
        return self.mapSize
