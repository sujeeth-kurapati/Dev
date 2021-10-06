from linked_list import Linkedlist

my_linkedlist = Linkedlist()
my_linkedlist.insert_node(5)
my_linkedlist.insert_node(3)
my_linkedlist.insert_node(2)
my_linkedlist.insert_node(6)
my_linkedlist.insert_node(4)

# print(my_linkedlist.head.value)
# print(my_linkedlist.head.next.value)
# print(my_linkedlist.head.next.next.value)
# print(my_linkedlist.head.next.next.next.value)
# print(my_linkedlist.head.next.next.next.next.value)

my_linkedlist.print_list_items()
print(my_linkedlist.count_nodes())       #getting node count using iterative method
print(my_linkedlist.count_nodes_rec())   #getting node count using recursive method
my_linkedlist.insert_node(7)
print(my_linkedlist.count_nodes_rec())

print(my_linkedlist.find_node(2))
print(my_linkedlist.find_node(9))