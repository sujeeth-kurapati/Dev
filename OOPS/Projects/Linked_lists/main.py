from linked_list import Linkedlist

my_linkedlist = Linkedlist()
my_linkedlist.insert_node(5)
my_linkedlist.insert_node(3)
my_linkedlist.insert_node(2)
my_linkedlist.insert_node(6)
my_linkedlist.insert_node(4)

print(my_linkedlist.head.value)
print(my_linkedlist.head.next.value)
print(my_linkedlist.head.next.next.value)
print(my_linkedlist.head.next.next.next.value)
print(my_linkedlist.head.next.next.next.next.value)