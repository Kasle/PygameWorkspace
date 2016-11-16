import pygame

class Manager:

    def __init__(self):
        self.objects = []

    def addObjects(self, objectList):
        for object in objectList:
            self.objects.append(object)

    def checkCollision(self, object1, object2):
        collideUpd = False
        if object1.coordY > 600 - (object1.radius):
            object1.coordY = 600 - (object1.radius)
            object1.yVel *= -1
            collideUpd = True
        elif object1.coordY < 0 + (object1.radius):
            object1.coordY = 0 + (object1.radius)
            object1.yVel *= -1
            collideUpd = True

        if object1.coordX > 800 - (object1.radius):
            object1.coordX = 800 - (object1.radius)
            object1.xVel *= -1
            collideUpd = True
        elif object1.coordX < 0 + (object1.radius):
            object1.coordX = 0 + (object1.radius)
            object1.xVel *= -1
            collideUpd = True

        if not type(object2) == int:
            if (abs(object1.coordX-object2.coordX)**2+abs(object1.coordY-object2.coordY)**2)**0.5 <= (object1.radius + object2.radius):
                print("Collision")

        if collideUpd == True:
            object1.xVel *= object1.restitution
            object1.yVel *= object1.restitution
            object1.rectifyValues()

    def manageCollisions(self):
        for startIndex in range(len(self.objects)-1):
            for object in self.objects[startIndex+1:]:
                self.checkCollision(self.objects[startIndex], object)
        self.checkCollision(self.objects[-1], 0)

    def managePhysics(self):
        self.manageCollisions()
        for object in self.objects:
            if object.type == 'P':
                if not object.isStatic:
                    object.applyGravity()

    def drawObjects(self):
        for object in self.objects:
            object.draw()

    def update(self):
        for object in self.objects:
            if object.type == 'D' or object.type == 'P':
                object.updatePosition()
        self.managePhysics()
        self.drawObjects()


