class Node:
    def __init__(self, key, value, next_node=None, prev_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
