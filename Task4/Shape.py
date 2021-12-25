
class Shape:
    def __init__(self, strokeWidth, strokeColor, fillColor ):
        self.strokeWidth=float(strokeWidth)
        self.strokeColor=strokeColor
        self.fillColor=fillColor

    def getStrokeWidth(self):
        return self.strokeWidth

    def getStrokeColor(self):
        return self.strokeColor

    def getFillColor(self):
        return self.fillColor

    def setStrokeWidth(self, StrokeWidth):
        self.strokeWidth=StrokeWidth

    def setStrokeColor(self, StrokeColor):
        self.strokeColor = StrokeColor

    def setFillColor(self, FillColor):
        self.fillColor = FillColor
