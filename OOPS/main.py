class House:

    def __init__(self,price,items):
        self.price = price
        self.items = items

class Circle:

    def __init__(self, radius, color = "Blue"):
        self.radius = radius
        self.color = color
        print(self)
        for item in self:
            print(item)


class Rectangle:

    def __init__(self, length, width, color = "Red"):
        self.length = length
        self.width = width
        self.color = color


class Movie:

    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating


cir = Circle(8)
print(cir.radius)
# for item in cir:
#     print(item)