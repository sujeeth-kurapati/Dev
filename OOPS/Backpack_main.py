class Backpack:

    max_num_items = 10 # class attribute

    def __init__(self, color, size):
        self.items = []
        self.color = color
        self.size = size
 

my_backpack = Backpack("blue", "Small")
your_backpack = Backpack("Red", "Large")


print(Backpack.max_num_items)
print(my_backpack.max_num_items)
print(your_backpack.max_num_items)