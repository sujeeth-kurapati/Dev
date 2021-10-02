class Point2D:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):  #here the self itself is an object and other is as well an object
        #pointA.__add__(pointB) --> this is how it is substituted
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point2D(new_x, new_y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    
pointA = Point2D(2,3)
pointB = Point2D(4,5)

pointC = pointA + pointB

print(pointC)