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
            
    def count_nodes(self):
        count = 0
        runner = self.head
        
        while runner is not None:
            count += 1
            runner = runner.next
        
        return count
    
    def count_nodes_rec(self):
        return self.count_nodes_recursive(self.head)
    
    def count_nodes_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.count_nodes_recursive(node.next)