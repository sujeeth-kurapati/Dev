class House:

    def __init__(self,price,items):
        self.price = price
        self.items = items


class Circle:

    VALID_COLORS = ("Red", "Green", "Blue", "Black") # we have considered this a tuple data structure since it is immutable

    def __init__(self, radius, color = "Blue"):
        self._radius = radius
        self._color = color

    def get_radius(self):
        print("Getter is being called")
        return self._radius

    def set_radius(self, new_radius):
        print("Setter is being called")
        if isinstance(new_radius, int) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Please valid value for the radius of the circle")

    radius = property(get_radius, set_radius) # Safe way of calling Non - Public variables with getter and setter implementation 

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print("Please enter a valid color")

    color = property(get_color, set_color)


class Rectangle:

    def __init__(self, length, width, color = "Red"):
        self.length = length
        self.width = width
        self.color = color


class Movie:
    
    id_counter = 1
    def __init__(self, title, year, language, rating):
        self._id = Movie.id_counter
        self._title = title
        self.year = year
        self.language = language
        self.rating = rating

        Movie.id_counter += 1

    def get_title(self): # created a seperate function to call the non public variable. this is the functionality of the getter
        return self._title


class Dog:

    def __init__(self, name, age):
        self._name = name
        self.age = age

    def get_name(self):
        return self._name
    
    def set_name(self, new_name): # Defined a setter function for updating the attribute value
        if isinstance(new_name, str): # we can addsome check conditions before assigning the values
            self._name = new_name
        else:
            print("Please enter a valid name for the Dog")


class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self._year = year   #by adding under score we declared it as an private variable

print(50*"*","Circle Class print variables",50*"*")
cir = Circle(8, "Red")
print(cir.radius) #here we dont need to update the attribute syntax to call the private variables since we are implementing "property" functionality
print(cir.color)
cir.radius += 1
print(cir.radius) 

print(50*"*","Car Class print variables",50*"*")
my_car = Car("Porsche", "911 Turbo S", 2021)
print(my_car._year)
 
print(50*"*","Movie Class print variables",50*"*")
my_movie = Movie("Pride and Prejudice", 2010, "English", 7.7)
your_movie = Movie("Tenet", 2020, "English", 8.4)
print(my_movie._id)
print(my_movie.get_title()) #Using the functionality of getter

print(50*"*","Dog Class print variables",50*"*")
my_dog = Dog("Nemo", 3)
print(my_dog.get_name())
print("Now we are updating the name of the dog")
my_dog.set_name("Flash")
print(my_dog.get_name())
my_dog.set_name(99) #if we pass a value other than string it will not be assigned since we are checking for the data type