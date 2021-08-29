class Human:
    species = 'Homosepians'
    def __init__(self,name,age):
        self.name = name 
        self.age = age


    def __str__(self): # this function gives the description of the class instance
        return f"{self.name} is {self.age} year old!"



class Asian(Human):
    def language(self, language='Japanese'):
        return f"{self.name}'s mother tounge is {language}"


class Hispanic(Human):
    def language(self, language='Spanish'):
        return f"{self.name}'s mother tounge is {language}"


class European(Human):
    def language(self, language='Spanish'):
        return f"{self.name}'s mother tounge is {language}"


# obj1 = Human('sujeeth',27)

# print(obj1.name)
# print(obj1.species)
# # obj1.age=23
# print(obj1.age)
# print(obj1)
# print(obj1.language('Telugu'))


obj1 = Asian('sujeeth',27)
obj2 = European('natasha',25)
print(obj2.language())
print(obj2)
# print('This is a new commit from Visual Studio')
# print("New addition on the Studio Code")
# print("this is from branch")
# print("import twitter")