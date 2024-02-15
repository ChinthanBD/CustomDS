class Node:
    def __init__(self, value, left=None, right=None, children=None):
        self.value = value
        self.left = left
        self.right = right
        self.children = children

    def getValue(self):
        return self.value

    def getChildren(self):
        return self.children

    def addToChildren(self, value):
        if isinstance(self.children, list):
            self.children.append(value)
            return True
        elif isinstance(self.children, set):
            self.children.add(value)
            return True
        else:
            return False
