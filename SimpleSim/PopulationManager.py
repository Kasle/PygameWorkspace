import pygame
import Functions as f
import random

class PopulationManager:

    def __init__(self, worldMap):
        self.settlements = []
        self.worldMap = worldMap
        self.tileMap = []
        self.generateTileMap()
        self.shouldUpdateTileMap = False
        self.placePositions = self.findPlaceablePositions()

    def tick(self):
        if self.shouldUpdateTileMap:
            self.updateTileMap()
        for i in self.settlements:
            i.tick(self.tileMap)
            self.updateTileMap()

    def addSettlement(self, position = [-1, -1], population = 1, name = 'NONE'):
        settlementLocation = position
        if settlementLocation == [-1, -1]:
            settlementLocation = self.placePositions.pop(random.randint(0, len(self.placePositions)-1))

        self.settlements.append(Settlement(settlementLocation, name, population))
        self.tileMap[settlementLocation[0]][settlementLocation[1]] = name

    def findPlaceablePositions(self):
        placeablePositions = []
        for tempX in range(self.worldMap.getSize()):
            for tempY in range(self.worldMap.getSize()):
                if self.tileMap[tempX][tempY] == '':
                    placeablePositions.append([tempX, tempY])
        return placeablePositions

    def generateTileMap(self):
        self.tileMap = [['X' for i in range(self.worldMap.getSize())] for j in range(self.worldMap.getSize())]
        for posX in range(self.worldMap.getSize()):
            for posY in range(self.worldMap.getSize()):
                if self.worldMap.foodMap[posX][posY] >= 0.7:
                    self.tileMap[posX][posY] = ''


    def updateTileMap(self):
        for settlement in self.settlements:
            for districtLayer in settlement.districtMap:
                for district in districtLayer:
                    self.tileMap[district.position[0]][district.position[1]] = settlement.settlementName
        self.shouldUpdateTileMap = False

class Settlement:

    def __init__(self, startPosition, settlementName = 'NONE', population = 1):
        self.settlementName = settlementName
        self.startPosition = startPosition
        self.districtMap = [[District(self.startPosition, 'residential')]]

    def tick(self, tileMap):
        print(len(self.districtMap))
        x = []
        for districtLayer in self.districtMap:
            for district in districtLayer:
                if not district.exp:
                    continue
                for perm in [[-1, 0],[1, 0],[0, -1],[0, 1]]:
                    if tileMap[district.position[0] + perm[0]][district.position[1] + perm[1]] == '':
                        x.append(District([district.position[0] + perm[0], district.position[1] + perm[1]],'residential'))
                district.exp = False
        self.districtMap.append(x)

class District:

    def __init__(self, position, type):
        self.position = position
        self.type = type
        self.exp = True




