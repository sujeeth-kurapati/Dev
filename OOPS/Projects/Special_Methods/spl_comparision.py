class Circle:
     
    def __init__(self, radius, color):
         self.radius = radius
         self.color = color
         
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __le__(self, other):
        return self.radius <= other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius
    
    def __ge__(self, other):
        return self.radius >= other.radius
    
    def __eq__(self, other):
        return (self.radius == other.radius and self.color == other.color)
         
    def __ne__(self, other):
        return (self.radius != other.radius or self.color != other.color)
    
    
circleA = Circle(7, "Red")
circleB = Circle(8, "Blue")
circleC = Circle(7, "Green")
circleD = Circle(7, "Red")


print(circleA == circleD) # Here the main catch is ---> we are comparing the instance objects directly

print(circleC == circleD)