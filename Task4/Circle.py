## PART A
import math
import Point
from Shape import Shape

class Circle(Shape):
    def __init__(self, centerPoint,radius):
        self.centerPoint=centerPoint
        self.radius=radius

    def area(self):
        return round(math.pi*(self.radius**2),2)

    def perimeter(self):
        return round(2*math.pi*self.radius, 2)

    def contains(self, givenPoint):
        if self.radius >= self.centerPoint.distance(givenPoint.getX(),givenPoint.getY() ):
            return True

    def toString(self):
        return "Circle ({},{}),{}".format(int(self.centerPoint.getX()), int(self.centerPoint.getY()),self.radius)

    def getCentroid(self):
        return self.centerPoint

    def getRadius(self):
        return self.radius

    def setCentroid(self,point_centroid):
        self.centerPoint=point_centroid

    def setRadious(self,radius):
        self.radius=radius