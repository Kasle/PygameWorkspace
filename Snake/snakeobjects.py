import pygame
import random

COLOR = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255)
    }

WIDTH = HEIGHT = 10

class BaseObject: #BaseObject

    def __init__(self, display, x, y):
        self.DISPLAY = display
        self.x = x
        self.y = y

class SnakeHead(BaseObject):

    def __init__(self, display, x, y):
        super().__init__(display, x, y)

    def move(self, directions):
        self.x += directions[0]*WIDTH
        self.y += directions[1]*HEIGHT

    def draw(self):
        pygame.draw.rect(self.DISPLAY, COLOR['WHITE'], [self.x, self.y, WIDTH, HEIGHT])

class SnakeBody(SnakeHead):

    def __inti__(self, display, x, y):
        super().__init__(display, x, y)
        self.nextX = x
        self.nextY = y

    def setNext(self, nextPosition):
        self.nextX = nextPosition[0]
        self.nextY = nextPosition[1]

    def move(self):
        self.x = self.nextX
        self.y = self.nextY

class Apple(BaseObject):

    def __init__(self, display, x, y):
        super().__init__(display, x, y)

    def jump(self, bounds):
        units = [bounds[0]/WIDTH, bounds[1]/HEIGHT]
        self.x = random.randint(5, units[0]-5)*WIDTH
        self.y = random.randint(5, units[1]-5)*HEIGHT

    def draw(self):
        pygame.draw.rect(self.DISPLAY, COLOR['RED'], [self.x, self.y, WIDTH, HEIGHT])
        
def coll(A, B):
    return A.x == B.x and A.y == B.y

def bound(A, BOUND):
    return A.x >= BOUND[0]-WIDTH or A.x <= 0 or A.y >= BOUND[1]-HEIGHT or A.y <= 0
