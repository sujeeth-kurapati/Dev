class Polygon:
    def __init__(self, sides, color):
        self.sides = sides
        self.color = color

class Square(Polygon):
    pass

class Triangle(Polygon):
    SIDES = 3
    def __init__(self, base, height, color):
        # Two ways of calling classes
        # Polygon.__init__(self, Triangle.SIDES, color)
        super().__init__(Triangle.SIDES, color)
        self.base = base
        self.height = height

class Mammal:
    def __init__(self, name, age, health, num_offspring, years_in_captivity):
        self.name = name
        self.age = age
        self.health = health
        self.num_offspring = num_offspring
        self.years_in_captivity = years_in_captivity

# Define the Panda class below this line

class Panda(Mammal):
    
    is_endangered = True
    
    def __init__(self,name, age, health, num_offspring, years_in_captivity, code):
        Mammal.__init__(self, name, age, health, num_offspring, years_in_captivity)
        self.code = code
        
class Professor:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def greet_students(self):
        print("Welcome to class!")

# Define your class below this line
class ScienceProfessor(Professor):
   
    def greet_students(self):
        print("Hi everyone! It's a great day to study Science!")
        Professor.greet_students(self)


science_professor = ScienceProfessor("Moses", 51, "Physics")
science_professor.greet_students()       


my_panda = Panda("Bloom", 12, "Good", 3, 7, "BR3476")

print(issubclass(Triangle, Polygon))
triangle = Triangle(12, 15, "Red")
print(triangle.sides)