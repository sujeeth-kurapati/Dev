#Sequence of elements links one to the other
# website followed for reference ----> https://realpython.com/linked-lists-python/
#Real world application for implementing  stacks, queues, graphs and lifecycle operation of operating system


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            # print(nodes)
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def add_first(self,node):
        node.next = self.head
        self.head = node

    def add_last(self,node):
        if self.head is None:
            self.head = node
        for item in self:
            pass
        item.next = node


# this repsent function prints all the objects in linked list as in the order they were assigned
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

# for iterating the contents in the linked list we are defining the loop
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

#Individually assign nodes and linking one another
# head_node = Node('s')
# # print(head_node.data)
# hd.head = head_node
# scnd_node = Node('u')
# thrd_node = Node('j')
# head_node.next = scnd_node
# scnd_node.next = thrd_node
#Passing the node values as a list
hd = LinkedList(['s','u','j','i'])
#adding element to the begining of the linked list
hd.add_first(Node(data='k'))
#adding element to the end of the linked list
hd.add_last(Node('l'))
# for item in hd:
#     print(item)
print(hd)