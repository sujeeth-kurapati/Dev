"""As part of Data Structures, we are implementing the fucntionality of arrays using other simple
data structures like dictionaries"""

class MyArray:
    
    def __init__(self):
        self.length = 0
        self.data = {}
        
    def add(self, item):
        """Add items into the array"""
        self.data[self.length] = item
        self.length =+ 1
        
    def pop(self):
        """Removes the items from the array"""
        del self.data[len(self.data) - 1]
        
    def len(self):
        """Return the length of the array"""
        return len(self.data)
        
            
m1 = MyArray()
m1.add('Hello')
m1.add('Wait')
print(m1.len())
print(m1.data)
# m1.pop()
# print(m1.data)