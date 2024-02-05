from tree_node import Node


class BST:
    def __init__(self) -> None:
        self.root = None
    
    def add_node(self, element):
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
        node = self.search_node(element)
        if not node:
            return None
        if not node.right and node.left:
            node.value = None
        elif not node.right and node.left:
            pass
        else:
            pass

    def max_height(self, source, height=0):
        temp = source
        if not temp:
            return height

        height = max(height, self.max_height(temp.right, height+1), self.max_height(temp.left, height+1))
        return height


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
    element_to_search = 50
    result = bst.search_node(element_to_search)
    if result:
        print(f"\nElement {element_to_search} found in the tree.")
    else:
        print(f"\nElement {element_to_search} not found in the tree.")

    element_to_search = 1201
    result = bst.search_node(element_to_search)
    if result:
        print(f"\nElement {element_to_search} found in the tree.")
    else:
        print(f"\nElement {element_to_search} not found in the tree.")

    # Max height of the tree
    height = bst.max_height(bst.root)
    print(f"\nMax height of the tree: {height}")


if __name__ == "__main__":
    main()