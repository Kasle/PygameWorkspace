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
        
        self.heightMap = self.generateHeightMap()
        self.moistureMap = self.generateMoistureMap()
        self.temperatureMap = self.generateTemperatureMap()
        #self.heightMap=self.temperatureMap
        #self.resourceMap = self.generateResourcemap()
        #self.biomeMap = self.generateBiomeMap()

    
    def generateHeightMap(self):
        
        tempMap = f.generateNoiseMap(self.heightSeed, self.mapSize, 0.008, 0.1, 1, 10, 0.75, 1.5) #Map Values
        
        for x in range(self.mapSize):
            for y in range(self.mapSize):
                absRange = min(self.mapSize/2.0, ((x-self.mapSize/2)**2 + (y-self.mapSize/2)**2)**0.5)
                heightMultiplier = - ( absRange / (self.mapSize/2.0) )**12 + 1
                #tempMap[x][y] *= heightMultiplier
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
        tempMap = []
        return tempMap


    def getSeed(self):
        return self.seed


    def getSize(self):
        return self.mapSize
