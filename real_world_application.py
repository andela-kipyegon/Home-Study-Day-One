
"""A real world problem with the use of OOP"""
"""Solves Perimeter and area for triangle square and rectangle"""

#Parent class Polygon
class Polygon():
    def __init__(self):
        pass
#Rectangle inherits from Polygon
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def getArea(self):
        return self.length * self.width

    def getPerimeter(self):
        return 2*(self.length+self.width)

#Triangle inherits from Polygon
class Triangle(Polygon):
    def __init__(self,side_1,side_2,side_3):
        self.a =side_1
        self.b =side_2
        self.c =side_3
    def getArea(self):
        s = (self.a+self.b+self.c) / 2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        return area
    def getPerimeter(self):
        return (self.a+self.b+self.c)

 #Square inherits from the rectangle    
class Square(Rectangle):
    def __init__(self, length):
        self.length = length

    def getArea(self):
        return self.length**2
 
    def getPerimeter(self):
        return 4*self.length

