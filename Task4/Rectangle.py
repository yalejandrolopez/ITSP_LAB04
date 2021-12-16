## PART A
import Point
from Shape import Shape

class Rectangle(Shape):
    def __init__(self, point, width, height ):
        self.topLeftPoint=point
        self.width=float(width)
        self.height=float(height)

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return(2*self.width+2*self.height)

    def contains(self, point):
        if self.topLeftPoint.getX()< point.getX() and self.topLeftPoint.getX()+ self.width> point.getX():
            if self.topLeftPoint.getY()< point.getY() and self.topLeftPoint.getY()+ self.height> point.getY():
                return True
            else:
                return False
        else:
            return False

    def centroid(self):
        return Point.Point(self.topLeftPoint.getX()+(self.width/2), self.topLeftPoint.getY() + (self.height / 2))

    def toString(self):
        return "(Point: {}, Width: {}, Height: {})".format(str(int (self.topLeftPoint.getX())) +"," +str(int((self.topLeftPoint.getY()))) , int(self.width), int(self.height))

    def getTopLeftPoint(self):
        return self.topLeftPoint

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setTopLeftPoint(self, point):
        self.topLeftPoint=point

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height
