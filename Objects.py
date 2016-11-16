import pygame

COLOR = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255)
    }

GRAVITY = 1

class BaseObject: #BaseObject

    def __init__(self, display, x, y):
        self.DISPLAY = display
        self.coordX = x
        self.coordY = y
        self.type = 'R'


class RigidObject(BaseObject): #RigidObject <= BaseObject

    def __init__(self, display, x, y):
        super().__init__(display, x, y)


class RigidRect(RigidObject): #Rectangle <= RigidObject <= BaseObject

    def __init__(self, display, x, y, width, height):
        super().__init__(display, x, y)
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(self.DISPLAY, COLOR['WHITE'], [int(self.coordX), int(self.coordY), self.width, self.height])


class RigidCircle(RigidObject): #Circle <= RigidObject <= BaseObject

    def __init__(self, display, x, y, radius):
        super().__init__(display, x, y)
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.DISPLAY, COLOR['WHITE'],[int(self.coordX), int(self.coordY)],self.radius)


class DynamicObject(BaseObject): #DynamicObject <= BaseObject

    def __init__(self, display, x, y, xvel, yvel):
        super().__init__(display, x, y)
        self.xVel = xvel
        self.yVel = yvel
        self.type = 'D'

    def updatePosition(self):
        self.coordX += self.xVel
        self.coordY += self.yVel
        self.rectifyValues()

    def rectifyValues(self):
        self.xVel = int(self.xVel)
        self.yVel = int(self.yVel)
        self.coordX = int(self.coordX)
        self.coordY = int(self.coordY)


class PhysicsObject(DynamicObject): #PhysicsObject <= DynamicObject <= BaseObject

    def __init__(self, display, x, y, xvel, yvel, mass, restitution):
        super().__init__(display, x, y, xvel, yvel)
        self.mass = mass
        self.restitution = restitution
        self.isStatic = False
        self.type = 'P'

    def updatePosition(self):
        self.coordX += self.xVel
        self.coordY += self.yVel
        self.rectifyValues()

    def applyGravity(self):
        self.yVel += GRAVITY

class PhysicsCircle(PhysicsObject): #PhysicsCircle <= PhysicsObject <= DynamicObject <= BaseObject

    def __init__(self, display, x, y, xvel, yvel, mass, restitution, radius):
        super().__init__(display, x, y, xvel, yvel, mass, restitution)
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.DISPLAY, COLOR['WHITE'],[int(self.coordX), int(self.coordY)],self.radius)

