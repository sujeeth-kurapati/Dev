class House:

    def __init__(self,price,items):
        self.price = price
        self.items = items


class Circle:

    def __init__(self, radius, color = "Blue"):
        self.radius = radius
        self.color = color


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


cir = Circle(8)
print(cir.radius)


my_car = Car("Porsche", "911 Turbo S", 2021)
print(my_car._year)
 

my_movie = Movie("Pride and Prejudice", 2010, "English", 7.7)
your_movie = Movie("Tenet", 2020, "English", 8.4)

print(my_movie._id)
print(my_movie.get_title()) #Using the functionality of getter

my_dog = Dog("Nemo", 3)
print(my_dog.get_name())
print("Now we are updating the name of the dog")
my_dog.set_name("Flash")
print(my_dog.get_name())
my_dog.set_name(99) #if we pass a value other than string it will not be assigned since we are checking for the data type