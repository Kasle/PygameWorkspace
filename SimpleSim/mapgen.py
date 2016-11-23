import noise
import random
import functions

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
        self.moistureMap = self.generateMoistureMap()
        #self.heightMap=self.moistureMap
        self.temperatureMap = self.generateTemperatureMap()
        #self.heightMap=self.temperatureMap
        #self.resourceMap = self.generateResourcemap()
        #self.biomeMap = self.generateBiomeMap()

    
    def generateHeightMap(self):
        tempMap = []
        offsetScale = random.random() * 100
        offsetX = random.random() * offsetScale
        offsetY = random.random() * offsetScale
        horizontalScale = 0.01
        verticalScale = 1.3
        runningMaxMin = [-1000, 1000]
        for x in range(self.mapSize):
            tempMap.append([])
            for y in range(self.mapSize):
                absRange = ((x-self.mapSize/2)**2 + (y-self.mapSize/2)**2)**0.5
                noiseValue = functions.translate(noise.pnoise2(x * horizontalScale + offsetX, y * horizontalScale + offsetY, 5, 0.3, 3), -1, 1, 0, 1)
                #noiseValue*= (-(2*absRange/self.mapSize)**4 + 1)*verticalScale
                tempMap[-1].append(max(-1, noiseValue))
        return tempMap

    def generateMoistureMap(self):
        tempMap = []
        offsetScale = random.random() * 100
        offsetX = random.random() * offsetScale
        offsetY = random.random() * offsetScale
        for x in range(self.mapSize):
            tempMap.append([])
            for y in range(self.mapSize):
                noiseValue = noise.pnoise2(x * 0.01 + offsetX, y * 0.01 + offsetY, 4, 0.6, 1.5) / 2 + 0.5
                noiseValue = min(max(0, (-0.8*self.heightMap[x][y] + 2.2*noiseValue )), 1)
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
                noiseValue = noise.pnoise2(x * 0.005 + offsetX, y * 0.005 + offsetY, 5, 0.7, 3)*30
                noiseValue = functions.translate(y, 0, self.mapSize, -30, 30) + noiseValue + functions.translate(max(0.5, self.heightMap[x][y]), 0.5, 1, 20, -20)
                tempMap[-1].append(noiseValue)
        print(max([max([j for j in i]) for i in tempMap]))
        return tempMap

    def generateResourceMap(self):
        tempMap = []
        offsetScale = random.random() * 100
        offsetX = random.random() * offsetScale
        offsetY = random.random() * offsetScale
        for x in range(self.mapSize):
            tempMap.append([])
            for y in range(self.mapSize):
                tempMap[-1].append(noise.pnoise2(x * 0.01 + offsetX, y * 0.01 + offsetY, 5, 0.6, 3) / 2 + 0.5)
        return tempMap

    def generateBiomeMap(self):
        tempMap = []
        return tempMap

    def getSeed(self):
        return self.seed

    def getSize(self):
        return self.mapSize
