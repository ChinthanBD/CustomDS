from node_tree import Node


class AvlTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursively(value, self.root)

    def _insert_recursively(self, value, current_node):
        if current_node is None:
            return Node(value)

        if value < current_node.get_value():
            current_node.left = self._insert_recursively(value, current_node.left)
        elif value > current_node.get_value():
            current_node.right = self._insert_recursively(value, current_node.right)

        # Update height and balance factor
        current_node = self._balance(current_node)

        return current_node

    def _balance(self, current_node):
        # Calculate the height of the node
        node_height = self._get_height(current_node)

        # Calculate the balance factor of the node
        balance_factor = self._get_balance_factor(current_node)

        # Left heavy
        if balance_factor > 1:
            if self._get_balance_factor(current_node.left) < 0:
                current_node.left = self._rotate_left(current_node.left)
            return self._rotate_right(current_node)

        # Right heavy
        if balance_factor < -1:
            if self._get_balance_factor(current_node.right) > 0:
                current_node.right = self._rotate_right(current_node.right)
            return self._rotate_left(current_node)

        return current_node

    def _rotate_left(self, parent_node):
        right_child = parent_node.right
        left_grandchild = right_child.left

        # Perform left rotation
        right_child.left = parent_node
        parent_node.right = left_grandchild

        return right_child

    def _rotate_right(self, parent_node):
        left_child = parent_node.left
        right_grandchild = left_child.right

        # Perform right rotation
        left_child.right = parent_node
        parent_node.left = right_grandchild

        return left_child

    def _get_height(self, current_node):
        if current_node is None:
            return 0
        return max(self._get_height(current_node.left), self._get_height(current_node.right)) + 1

    def _get_balance_factor(self, current_node):
        if current_node is None:
            return 0
        return self._get_height(current_node.left) - self._get_height(current_node.right)


def main():
    # Create an instance of AvlTree
    avl_tree = AvlTree()

    # Insert some values into the AVL tree
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        avl_tree.insert(value)

    # Print the AVL tree
    print("AVL Tree:")
    print_tree(avl_tree.root)


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(" " * 4 * level + "->", node.get_value())
        print_tree(node.left, level + 1)


if __name__ == "__main__":
    main()
