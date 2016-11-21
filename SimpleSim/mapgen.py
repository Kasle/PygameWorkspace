import noise
import random

class mapManager:

    def __init__(self, size, seed):
        self.seed = seed
        self.mapSize = size
        random.seed(self.seed)
        self.heightMap = []
        self.temperatureMap = []
        self.moistureMap = []
        self.resourceMap = []
        self.biomeMap = []
        self.generateMaps()

    def generateMaps(self):
        self.heightMap = self.generateHeightMap()
        #self.moistureMap = self.generateMoistureMap()
        #self.temperatureMap = self.generateTemperatureMap()
        #self.resourceMap = self.generateResourcemap()
        #self.biomeMap = self.generateBiomeMap()

    def generateHeightMap(self):
        tempMap = []
        offsetScale = random.random() * 100
        offsetX = random.random() * offsetScale
        offsetY = random.random() * offsetScale
        horizontalScale = 0.01
        verticalScale = 1.3
        for x in range(self.mapSize):
            tempMap.append([])
            for y in range(self.mapSize):
                absRange = ((x-self.mapSize/2)**2 + (y-self.mapSize/2)**2)**0.5
                noiseValue = noise.pnoise2(x * horizontalScale + offsetX, y * horizontalScale + offsetY, 5, 0.3, 3) / 2 + 0.5
                noiseValue *= (-(2*absRange/self.mapSize)**4 + 1)*verticalScale
                tempMap[-1].append(noiseValue)
        return tempMap

    def generateTemperatureMap(self):
        tempMap = []
        offsetScale = random.random() * 100
        offsetX = random.random() * offsetScale
        offsetY = random.random() * offsetScale
        for x in range(self.mapSize):
            tempMap.append([])
            for y in range(self.mapSize):
                tempMap[-1].append(noise.pnoise2(x * 0.01 + offsetX, y * 0.01 + offsetY, 3, 0.4, 2) / 2 + 0.5)
        return tempMap

    def generateMoistureMap(self):
        tempMap = []
        offsetScale = random.random() * 100
        offsetX = random.random() * offsetScale
        offsetY = random.random() * offsetScale
        for x in range(self.mapSize):
            tempMap.append([])
            for y in range(self.mapSize):
                tempMap[-1].append(noise.pnoise2(x * 0.01 + offsetX, y * 0.01 + offsetY, 3, 0.4, 2) / 2 + 0.5)
        return tempMap

    def generateResourcemap(self):
        tempMap = []
        offsetScale = random.random() * 100
        offsetX = random.random() * offsetScale
        offsetY = random.random() * offsetScale
        for x in range(self.mapSize):
            tempMap.append([])
            for y in range(self.mapSize):
                tempMap[-1].append(noise.pnoise2(x * 0.01 + offsetX, y * 0.01 + offsetY, 3, 0.4, 2) / 2 + 0.5)
        return tempMap

    def generateBiomeMap(self):
        tempMap = []
        offsetScale = random.random() * 100
        offsetX = random.random() * offsetScale
        offsetY = random.random() * offsetScale
        for x in range(self.mapSize):
            tempMap.append([])
            for y in range(self.mapSize):
                tempMap[-1].append(noise.pnoise2(x * 0.01 + offsetX, y * 0.01 + offsetY, 3, 0.4, 2) / 2 + 0.5)
        return tempMap

    def getSeed(self):
        return self.seed

    def getSize(self):
        return self.mapSize
