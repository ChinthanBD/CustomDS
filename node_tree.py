class Node:
    def __init__(self, value=None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
