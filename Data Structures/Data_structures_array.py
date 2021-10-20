"""As part of Data Structures, we are implementing the fucntionality of arrays using other simple
data structures like dictionaries"""

class MyArray:
    
    def __init__(self):
        # self.length = 0
        self.data = {}
        
    def get(self, index):
        """Returns the value at the location"""
        return self.data[index-1]
        
    def add(self, item):
        """Add items into the array"""
        self.data[self.len()] = item
        
    def pop(self):
        """Removes the items from the array"""
        del self.data[len(self.data) - 1]
        # self.length =- 1
        
    def len(self):
        """Return the length of the array"""
        return len(self.data)
    
    def delete(self, index):
        """Delete the content at aspecified location"""
        self.shift_items(index)
        
    def shift_items(self, index):
        length = self.len()
        while index < length:
            self.data[index-1] = self.data[index]
            index=index+1
        self.pop()

            
m1 = MyArray()
m1.add('Hello')
print(m1.data)
m1.add('Wait')
print(m1.data)
m1.add('yes')
print(m1.data)
m1.add('please')
# print(m1.len())
print(m1.data)
m1.delete(2)
print(m1.data)
# print(m1.get(2))