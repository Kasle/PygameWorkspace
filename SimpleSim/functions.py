import noise
import random

def fMap(value, a, b, A, B):
    firstScale = b - a
    secondScale = B-A
    position = value - a
    position = position / float(firstScale)
    return secondScale * position + A

def generateNoiseMap(seed = 0,size = 1, scale = 0.01, outputMax = -1, outputMin = 1, octaves=1, persistence=0.5, lacunarity=2.0):
    
    random.seed(seed)

    offX = ( random.random() * 100 ) - 50
    offY = ( random.random() * 100 ) - 50
    
    mx = -1000
    mn = 10000

    tempMap = []
    
    for x in range(size):
        tempMap.append([])
        for y in range(size):
            tempValue = noise.pnoise2(x * scale + offX, y * scale + offY, octaves, persistence, lacunarity)
            mx = max(mx, tempValue)
            mn = min(mn, tempValue)
            tempMap[-1].append(tempValue)

    for x in range(size):
         for y in range(size):
             tempMap[x][y] = fMap(tempMap[x][y], mn, mx, outputMin, outputMax)

    return tempMap
