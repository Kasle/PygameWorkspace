import pygame
import snakeobjects
import random

pygame.init()

COLOR = {
    'WHITE' : (255, 255, 255),
    'BLACK' : (0, 0, 0),
    'RED' : (255, 0, 0),
    'GREEN' : (0, 255, 0),
    'BLUE' : (0, 0, 255)
    }

screenSize = [800, 600]

clock = pygame.time.Clock()

print('Game Start...\n')

gameDisplay = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Slither")

##Game Loop

gameExit = False

snake = snakeobjects.SnakeHead(gameDisplay, 300, 300)

snakeBody = []

direct = [1, 0]

A = snakeobjects.Apple(gameDisplay, 0, 0)
A.jump(screenSize)

points = 0
highScore = 0

try:
    hsSheet = open('hs', 'r')
    highScore = int(hsSheet.readline())
    hsSheet.close()
except:
    pass

while not gameExit:
    for event in pygame.event.get(): ##Event Handler
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == 273: #UP
                if not direct == [0, 1]:
                    direct = [0, -1]
            elif event.key == 274: #DOWN
                if not direct == [0, -1]:
                    direct = [0, 1]
            elif event.key == 275: #RIGHT
                if not direct == [-1, 0]:
                    direct = [1, 0]
            elif event.key == 276: #LEFT
                if not direct == [1, 0]:
                    direct = [-1, 0]
            #elif event.key == 32: #SPACE
            #    snakeBody.append(snakeobjects.SnakeBody(gameDisplay, snake.x, snake.y))
            else: #KEYPRESS
                print('KEYDOWN',event.key)
                

    if A.x == snake.x and A.y == snake.y:
        A.jump(screenSize)
        points+=1
        if points > highScore:
            hsSheet = open('hs', 'w')
            hsSheet.write(str(points))
            hsSheet.close()
            highScore = points
        print('Score:',points, '| High Score:',highScore)
        [snakeBody.append(snakeobjects.SnakeBody(gameDisplay, snake.x, snake.y)) for i in range(points)]
    
    gameDisplay.fill(COLOR['BLACK'])

    if snakeBody:
        snakeBody[0].setNext((snake.x, snake.y))
        for i in range(1,len(snakeBody)):
            snakeBody[i].setNext((snakeBody[i-1].x, snakeBody[i-1].y))
            
        [seg.move() for seg in snakeBody]
        [seg.draw() for seg in snakeBody]

    snake.move(direct)

    if snakeobjects.bound(snake, screenSize):
        gameExit = True
    for seg in snakeBody:
        if snakeobjects.coll(snake, seg):
            gameExit = True

    A.draw()
    snake.draw()
    pygame.display.update()

    clock.tick(20)

pygame.quit()

print('\nGame Over...')
