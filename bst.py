from tree_node import Node


class BST:
    def __init__(self) -> None:
        self.head = None
    
    def add_node(self, element):
        if not self.head:
            self.head = Node(element)
            return True
        
        temp = self.head
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
    
    def pre_order_traversal(self, node):
        temp = node
        if temp:
            print(temp.value)
            self.pre_order_traversal(temp.left)
            self.pre_order_traversal(temp.right)
        
    def post_order_traversal(self, node):
        temp = node
        if temp:
            self.pre_order_traversal(temp.left)
            self.pre_order_traversal(temp.right)
            print(temp.value)

    def in_order_traversal(self, node):
        temp = node
        if temp:
            self.pre_order_traversal(temp.left)
            print(temp.value)
            self.pre_order_traversal(temp.right)


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

    # Pre-order Traversal
    print("Pre-order Traversal:")
    bst.pre_order_traversal(bst.head)

    # In-order Traversal
    print("\nIn-order Traversal:")
    bst.in_order_traversal(bst.head)

    # Post-order Traversal
    print("\nPost-order Traversal:")
    bst.post_order_traversal(bst.head)


if __name__ == "__main__":
    main()