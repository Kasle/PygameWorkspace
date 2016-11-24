import noise
import random
import functions as f

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
        self.generateMaps()


    def generateMaps(self):
        print("Generating Height Map...")
        self.heightMap = self.generateHeightMap()
        print("Generating Moisture Map...")
        self.moistureMap = self.generateMoistureMap()
        print("Generating Temperature Map...")
        self.temperatureMap = self.generateTemperatureMap()
        #self.heightMap=self.temperatureMap
        #self.resourceMap = self.generateResourcemap()
        print("Generating Biome Map...")
        self.biomeMap = self.generateBiomeMap()
        print("Generation Complete.")

    
    def generateHeightMap(self):
        
        tempMap = f.generateNoiseMap(self.heightSeed, self.mapSize, 0.008, 0.2, 1, 10, 0.75, 1.5) #Map Values
        
        for x in range(self.mapSize):
            for y in range(self.mapSize):
                absRange = min(self.mapSize/2.0, ((x-self.mapSize/2)**2 + (y-self.mapSize/2)**2)**0.5)
                heightMultiplier = - ( absRange / (self.mapSize/2.0) )**12 + 1
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
                tempMap[x][y] = tempMap[x][y] + f.fMap(y, 0, self.mapSize, -15, 40) + 0.7*f.fMap(self.moistureMap[x][y], 0, 1, 0, 10) + min(0, f.fMap(self.heightMap[x][y], 0, 1, 50, -30))
            
        return tempMap


    def generateResourceMap(self):
        
        tempMap = f.generateNoiseMap(self.moistureSeed, self.mapSize, 0.006, 0, 1, 5, 0.4, 1.5)
        
        for x in range(self.mapSize):
            for y in range(self.mapSize):
                tempMap[x][y] = tempMap[x][y]
            
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
                        tempMap[x][y] = 'frozenWater'
                    else:
                        tempMap[x][y] = 'snow'
                elif self.heightMap[x][y] < 0.5:
                    tempMap[x][y] = 'water'
                elif self.temperatureMap[x][y] < 5:
                    if self.moistureMap[x][y] < 0.3:
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
                elif self.temperatureMap[x][y] < 25:
                    if self.moistureMap[x][y] < 0.2:
                        tempMap[x][y] = 'barrenPlains'
                    elif self.moistureMap[x][y] < 0.4:
                        tempMap[x][y] = 'grassPlains'
                    else:
                        tempMap[x][y] = 'boreal'
                elif self.temperatureMap[x][y] < 27:
                    if self.moistureMap[x][y] < 0.3:
                        tempMap[x][y] = 'barrenPlains'
                    else:
                        tempMap[x][y] = 'savanna'
                elif self.temperatureMap[x][y] < 30:
                    if self.moistureMap[x][y] < 0.5:
                        tempMap[x][y] = 'wildPlains'
                    else:
                        tempMap[x][y] = 'boreal'
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


    def getSeed(self):
        return self.seed


    def getSize(self):
        return self.mapSize
