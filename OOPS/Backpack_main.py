class Backpack:

    max_num_items = 10 # class attribute

    def __init__(self, color, size):
        self._items = []  #making item attribute as private
        self.__color = color #Concept of name mangaling -- change the name of the attribute
        self.size = size

    @property
    def items(self):
        print("In the Getter")
        return self._items

    @items.setter
    def items(self, new_item):
        print("In the Setter")
        if isinstance(new_item, list):
            self._items = new_item
        else:
            print("Please enter a valid item")

my_backpack = Backpack("blue", "Small")
your_backpack = Backpack("Red", "Large")


print(Backpack.max_num_items)
print(my_backpack.max_num_items)
print(your_backpack.max_num_items)
#print(my_backpack.color) --> This does not work since we are changing the name
print(my_backpack._Backpack__color)
print(my_backpack.items)
my_backpack.items = ["Biscuit Packet"] 
print(my_backpack.items)