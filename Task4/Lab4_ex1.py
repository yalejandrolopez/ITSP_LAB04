import unittest
import Point
import Rectangle
import Circle
import math

class TestPoint(unittest.TestCase):

    def test_get_X(self):
        test_point  =  Point.Point(15, 35)
        self.assertEqual(15, test_point.getX())
        
    def test_get_Y(self):
        test_point  =  Point.Point(15, 35)
        self.assertEqual(35, test_point.getY())

    def test_setPosition(self):
        test_point = Point.Point(15, 35)
        x1 = 10
        y1 = 20
        test_point=test_point.setPosition(x1, y1)
        self.assertEqual(20, test_point.getY())
        self.assertEqual(10, test_point.getX())

    def test_toString(self):
        test_point = Point.Point(15, 35)
        self.assertEqual("(15,35)" , test_point.toString())

    def test_distance(self):
        test_point = Point.Point(15, 35)
        x2=30
        y2=40
        dis=test_point.distance(x2, y2)
        self.assertEqual( round(math.sqrt(pow(15 - 30, 2) + pow(35 - 40, 2)), 2)  , dis)
    
    def test_setX(self):
        test_point  =  Point.Point(15, 35)
        test_point.setX(20)
        self.assertEqual(20, test_point.getX())
        
    def test_setY(self):
        test_point  =  Point.Point(15, 35)
        test_point.setY(50)
        self.assertEqual(50, test_point.getY())

    def test_getStrokeWidth(self):
        test_point = Point.Point(15, 35)
        test_point.strokeWidth=4
        self.assertEqual(4, test_point.getStrokeWidth())

    def test_setStrokeWidth(self):
        test_point = Point.Point(15, 35)
        test_point.setStrokeWidth(10)
        self.assertEqual(10, test_point.strokeWidth)

    def test_getStrokeColor(self):
        test_point = Point.Point(15, 35)
        test_point.setStrokeColor('red')
        self.assertEqual('red', test_point.getStrokeColor())

    def test_setStrokeColor(self):
        test_point = Point.Point(15, 35)
        test_point.setStrokeColor('red')
        self.assertEqual('red', test_point.strokeColor)

    def test_getFillColor(self):
        test_point = Point.Point(15, 35)
        test_point.setFillColor('black')
        self.assertEqual('black', test_point.getFillColor())

    def test_setFillColor(self):
        test_point = Point.Point(15, 35)
        test_point.fillColor='black'
        self.assertEqual('black', test_point.getFillColor())


class TestRectangle(unittest.TestCase):

    def test_area(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        self.assertEqual(10*10, test_rec.area())

    def test_perimeter(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        self.assertEqual(10+10+10+10, test_rec.perimeter())

    def test_contains(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        self.assertEqual(False, test_rec.contains(Point.Point(100,100) ))

    def test_centroid(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        self.assertEqual(20, test_rec.centroid().getX() )
        self.assertEqual(40, test_rec.centroid().getY())

    def test_toString(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        self.assertEqual("(Point: 15,35, Width: 10, Height: 10)", test_rec.toString())

    def test_getTopLeftPoint(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        self.assertEqual(15, test_rec.getTopLeftPoint().getX())
        self.assertEqual(35, test_rec.getTopLeftPoint().getY())

    def test_getWidth(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        self.assertEqual(10, test_rec.getWidth())

    def test_getHeight(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        self.assertEqual(10, test_rec.getHeight())

    def test_setTopLeftPoint(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        test_rec.setTopLeftPoint(Point.Point(20,20))
        self.assertEqual(20, test_rec.topLeftPoint.getX())
        self.assertEqual(20, test_rec.topLeftPoint.getY())

    def test_setWidth(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        test_rec.setWidth(20)
        self.assertEqual(20, test_rec.width)

    def test_setHeight(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        test_rec.setHeight(20)
        self.assertEqual(20, test_rec.height)

    def test_getStrokeWidth(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        test_rec.strokeWidth = 4
        self.assertEqual(4, test_rec.getStrokeWidth())

    def test_setStrokeWidth(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        test_rec.setStrokeWidth(10)
        self.assertEqual(10, test_rec.strokeWidth)

    def test_getStrokeColor(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        test_rec.setStrokeColor('red')
        self.assertEqual('red', test_rec.getStrokeColor())

    def test_setStrokeColor(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        test_rec.setStrokeColor('red')
        self.assertEqual('red', test_rec.strokeColor)

    def test_getFillColor(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        test_rec.setFillColor('black')
        self.assertEqual('black', test_rec.getFillColor())

    def test_setFillColor(self):
        test_rec = Rectangle.Rectangle(Point.Point(15, 35), 10, 10)
        test_rec.fillColor = 'black'
        self.assertEqual('black', test_rec.getFillColor())

class TestCircle(unittest.TestCase):

    def test_area(self):
        test_cir = Circle.Circle(Point.Point(15, 35), 10)
        self.assertEqual(round(math.pi * 10*10, 2), test_cir.area())

    def test_perimeter(self):
        test_cir = Circle.Circle(Point.Point(15, 35), 10)
        self.assertEqual(round(2*math.pi*10, 2), test_cir.perimeter())

    def test_contains(self):
        test_cir = Circle.Circle(Point.Point(15, 35), 10)
        self.assertEqual(True, test_cir.contains(Point.Point(16,36) ))

    def test_toString(self):
        pt = Point.Point(15, 35)
        test_cir = Circle.Circle(pt, 10)
        self.assertEqual("Circle (15,35),10", test_cir.toString())

    def test_getCentroid(self):
        test_cir = Circle.Circle(Point.Point(15, 35), 10)
        self.assertEqual(15, test_cir.getCentroid().getX())
        self.assertEqual(35, test_cir.getCentroid().getY())

    def test_getRadius(self):
        pt=Point.Point(15,35)
        test_cir = Circle.Circle(pt, 10)
        self.assertEqual(10, test_cir.getRadius())

    def test_setCentroid(self):
        test_cir = Circle.Circle(Point.Point(15, 35), 10)
        test_cir.setCentroid(Point.Point(10,10))
        self.assertEqual(10, test_cir.centerPoint.getX())
        self.assertEqual(10, test_cir.centerPoint.getY())

    def test_setRadious(self):
        test_cir = Circle.Circle(Point.Point(15, 35), 10)
        test_cir.setRadious(10)
        self.assertEqual(10, test_cir.radius)

    def test_getStrokeWidth(self):
        test_cir = Circle.Circle(Point.Point(15, 35), 10)
        test_cir.strokeWidth = 4
        self.assertEqual(4, test_cir.getStrokeWidth())

    def test_setStrokeWidth(self):
        test_cir = Circle.Circle(Point.Point(15, 35), 10)
        test_cir.setStrokeWidth(10)
        self.assertEqual(10, test_cir.strokeWidth)

    def test_getStrokeColor(self):
        test_cir = Circle.Circle(Point.Point(15, 35), 10)
        test_cir.setStrokeColor('red')
        self.assertEqual('red', test_cir.getStrokeColor())

    def test_setStrokeColor(self):
        test_cir = Circle.Circle(Point.Point(15, 35), 10)
        test_cir.setStrokeColor('red')
        self.assertEqual('red', test_cir.strokeColor)

    def test_getFillColor(self):
        test_cir = Circle.Circle(Point.Point(15, 35), 10)
        test_cir.setFillColor('black')
        self.assertEqual('black', test_cir.getFillColor())

    def test_setFillColor(self):
        test_cir = Circle.Circle(Point.Point(15, 35), 10)
        test_cir.fillColor = 'black'
        self.assertEqual('black', test_cir.getFillColor())

if __name__ == '__main__':
     unittest.main()