from tree_node import Node
from enum import Enum


class TraversalType(Enum):
    PRE_ORDER_TRAVERSAL = "preorder"
    POST_ORDER_TRAVERSAL = "postorder"
    IN_ORDER_TRAVERSAL = "inorder"


class BST:
    def __init__(self) -> None:
        self.root = None
    
    def add_node(self, element):
        '''
        If any element is added which is already present(duplicate)
        then it will be added to right child of the existing node
        '''
        if not self.root:
            self.root = Node(element)
            return True
        
        temp = self.root
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
        self._traverse(node, traversal_type=TraversalType.PRE_ORDER_TRAVERSAL.value)

    def post_order_traversal(self, node):
        self._traverse(node, traversal_type=TraversalType.POST_ORDER_TRAVERSAL.value)

    def in_order_traversal(self, node):
        self._traverse(node, traversal_type=TraversalType.IN_ORDER_TRAVERSAL.value)

    def _traverse(self, node, traversal_type):
        if not node:
            return
        if traversal_type == TraversalType.PRE_ORDER_TRAVERSAL.value:
            print(node.value)
        self._traverse(node.left, traversal_type)
        if traversal_type == TraversalType.IN_ORDER_TRAVERSAL.value:
            print(node.value)
        self._traverse(node.right, traversal_type)
        if traversal_type == TraversalType.POST_ORDER_TRAVERSAL.value:
            print(node.value)

    def search_node(self, element):
        if not self.root:
            return None
        temp = self.root
        while temp:
            if temp.value == element:
                return temp
            elif element < temp.value:
                temp = temp.left
            else:
                temp = temp.right

        return None

    def delete_node(self, element):
        # Find the node to delete
        current = self.root
        parent = None
        while current and current.value != element:
            parent = current
            if element < current.value:
                current = current.left
            else:
                current = current.right

        # If the node is not found, return
        if current is None:
            return

        # Case 1: Node has no children
        if not current.left and not current.right:
            if current != self.root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None

        # Case 2: Node has one child
        elif current.left is None or current.right is None:
            if current.left:
                child = current.left
            else:
                child = current.right
            if current != self.root:
                if parent.left == current:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child

        # Case 3: Node has two children
        else:
            # Find the inorder successor (the smallest node in the right subtree)
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left

            # Replace the value of the node to be deleted with the value of the successor
            current.value = successor.value

            # Delete the successor (it has at most one right child)
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

    def max_height_from_node(self, node=None):
        if node is None:
            return 0
        else:
            left_height = self.max_height_from_node(node.left)
            right_height = self.max_height_from_node(node.right)
            return max(left_height, right_height) + 1


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
    bst.pre_order_traversal(bst.root)

    # In-order Traversal
    print("\nIn-order Traversal:")
    bst.in_order_traversal(bst.root)

    # Post-order Traversal
    print("\nPost-order Traversal:")
    bst.post_order_traversal(bst.root)

    # Searching for an element
    element_to_search = 1201
    result = bst.search_node(element_to_search)
    if result:
        print(f"\nElement {element_to_search} found in the tree.")
    else:
        print(f"\nElement {element_to_search} not found in the tree.")

    # Max height of the tree
    height = bst.max_height_from_node(bst.root)
    print(f"\nMax height of the tree: {height}")

    # Deleting a node
    element_to_delete = 30
    print(f"\nDeleting node with element {element_to_delete}:")
    bst.delete_node(element_to_delete)

    # In-order Traversal after deletion
    print("\nIn-order Traversal after deletion:")
    bst.in_order_traversal(bst.root)


if __name__ == "__main__":
    main()

