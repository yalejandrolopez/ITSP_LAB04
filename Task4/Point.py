## PART A
import math
from Shape import Shape

class Point(Shape):
    def __init__(self, x,y):
        self.x=float(x)
        self.y=float(y)

    def setPosition(self, x,y):
        self.x = x
        self.y = y
        return self

    def distance(self,x2,y2):
        return round(math.sqrt(pow(self.x - x2, 2) + pow(self.y - y2, 2)), 2)

    def toString(self):
        return "({},{})".format(self.x, self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self,x):
        self.x=x

    def setY(self, y):
        self.y=y
