from node import Node


class Linkedlist:
    
    def __init__(self):
        self.head = None
    
    def insert_node(self,value):
        
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value <= self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            previous = self.head
            runner = self.head.next
            
            while (runner is not None) and (value > runner.value):
                previous = runner
                runner = runner.next
                
            new_node.next = runner   
            previous.next = new_node
            
    def print_list_items(self):
        
        if self.head is None:
            print("Empty Linked List")
        else:
            runner = self.head
            while runner is not None:
                print(runner.value, end=" ")
                runner = runner.next
            print("\n")