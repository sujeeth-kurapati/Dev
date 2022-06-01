class Node:
    
    def __init__(self, value) -> None:
        self.root = value
        self.left = None
        self.right = None
        
def insert_node(nd, inst_val):
    if nd:
        if inst_val < nd.root:
            nd.left = insert_node(nd.left, inst_val)
        elif inst_val > nd.root:
            nd.right = insert_node(nd.right, inst_val)
    else:
        nd = Node(inst_val)
    return nd
    
def print_traversal(type, value): 
    if type == "preorder":
        pre_order(value)
    elif type == "inorder":
        in_order(value)
    elif type == "postorder":
        post_order(value)
    else:
        print("Enter correct type of order")

        
def pre_order(value):
    if value:
        print(str(value.root),end=' ')
        pre_order(value.left)
        pre_order(value.right)

        
def in_order(value):
    if value:
        in_order(value.left)
        print(str(value.root),end=' ')
        in_order(value.right)

        
def post_order(value):
    if value:
        post_order(value.left)
        post_order(value.right)
        print(str(value.root),end=' ')

        
# r = Node(5)
# # tre.left = Node(2)
# # tre.right = Node(7)
# # print_traversal("preorder", tre)
# r = insert_node(r, 4)


r = Node(50)
r = insert_node(r, 30)
r = insert_node(r, 20)
r = insert_node(r, 40)
r = insert_node(r, 70)
r = insert_node(r, 60)
r = insert_node(r, 80)

print_traversal("inorder", r)