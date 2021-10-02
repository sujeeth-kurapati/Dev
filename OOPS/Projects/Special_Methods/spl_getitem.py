class Bookshelf:
    
    def __init__(self):
        self.content = [[], [], []] #left most inner represent hte lower shelf and right most represent top shelf
        
    def add_book(self, level, book):
        self.content[level].append(book)
        
    def take_book(self, level, book):
        self.content[level].remove(book)
        
    def __getitem__(self, level):
        # obj[index] ---> obj.__getitem__(index)
        return self.content[level]

book = Bookshelf()

book.add_book(0, "Pride and Prejudice")
book.add_book(1, "Wings of Fire")
book.add_book(2, "The Alchemist")    

print(book[0])