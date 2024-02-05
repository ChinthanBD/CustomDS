from tree_node import Node

class BST:
    def __init__(self) -> None:
        self.head = None
    
    def add_node(self, element):
        if not self.head:
            self.head = Node(element)
            return True
        
        temp =  self.head
        while temp:
            if element < temp.value:
                if not temp.left:
                    temp.left = Node(element)
                    return True
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = Node(element)
                    return True
                temp = temp.right


def main():
    # Creating a Binary Search Tree object
    bst = BST()
    
    # Adding nodes to the Binary Search Tree
    bst.add_node(50)
    bst.add_node(30)
    bst.add_node(70)
    bst.add_node(20)
    bst.add_node(40)
    bst.add_node(60)
    bst.add_node(80)