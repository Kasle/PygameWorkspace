import pygame
import Functions
import MapManager
import Renderer
import PopulationManager

class World:

    def __init__(self, display, worldSize, startPopulation = 0, seed = 0):
        self.display = display
        self.worldSize = worldSize
        self.startPopulation = startPopulation
        self.mapSeed = seed
        self.create()
        self.shouldUpdateRender = True

    def create(self):
        self.worldMap = MapManager.MapManager(self.worldSize, self.mapSeed)
        self.populationManager = PopulationManager.PopulationManager(self.worldMap)
        print('Adding Population...')
        for count in range(self.startPopulation):
            self.populationManager.addSettlement()

    def tick(self):
        print('tick')
        if self.shouldUpdateRender:
            self.render()
            self.shouldUpdateRender = False
        self.populationManager.tick()
        self.shouldUpdateRender = True

    def render(self):
        Renderer.colorBiomes(self.display,self.worldMap, 'h')
        Renderer.colorSettlements(self.display, self.populationManager.settlements)