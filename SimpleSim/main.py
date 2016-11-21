import pygame
import random
from mapgen import mapManager

print(pygame.init())  ##(SUCCESS, FAILURE)

COLOR = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'YELLOW': (255, 255, 0)
}

mapXY = 800

map = mapManager(mapXY, 0)

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode([mapXY, mapXY], pygame.RESIZABLE)
pygame.display.set_caption("Erador")

##Game Loop

gameExit = False

while not gameExit:
    for event in pygame.event.get():  ##Event Handler
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(COLOR['BLACK'])

    for x in range(len(map.heightMap)):
        for y in range(len(map.heightMap[x])):
            if map.heightMap[x][y] < 0.5:
                gameDisplay.set_at((x, y), (0, 0, 200))
            elif map.heightMap[x][y] < 0.505:
                gameDisplay.set_at((x, y), (255, 255, 0))
            elif map.heightMap[x][y] < 0.7:
                gameDisplay.set_at((x, y), (0, 200, 0))
            elif map.heightMap[x][y] < 0.85:
                gameDisplay.set_at((x, y), (180, 180, 180))
            else:
                gameDisplay.set_at((x, y), (255, 255, 255))

    pygame.display.update()

    clock.tick(1)

pygame.quit()

quit()
