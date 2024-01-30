from static_array import StaticArray


class Stack:
    def __init__(self, size):
        # TC: O(1)
        self.size = size
        self.array = StaticArray(size)
        self.occupied_size = 0

    def push(self, element):
        # TC: O(1)
        if self.occupied_size != self.size:
            self.array.insert(element, self.occupied_size)
            self.occupied_size += 1
            return True
        return False

    def pop(self):
        # TC: O(1)
        if self.occupied_size == 0:
            return False
        self.array.delete(self.occupied_size)
        self.occupied_size -= 1

    def peek(self):
        # TC: O(1)
        if self.occupied_size == 0:
            return None
        return self.array.get(self.occupied_size)


def main():
    # Create a stack with size 5
    stack = Stack(5)

    # Push elements onto the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    # Try pushing more elements than the stack size
    result = stack.push(6)
    print("Pushing element onto full stack:", result)  # Expect: False

    # Peek at the top element
    top_element = stack.peek()
    print("Top element:", top_element)  # Expect: 5

    # Pop elements from the stack
    while stack.occupied_size > 0:
        popped_element = stack.pop()
        print("Popped element:", popped_element)  # Expect: 5, 4, 3, 2, 1

    # Try popping from an empty stack
    result = stack.pop()
    print("Popping from empty stack:", result)  # Expect: False


if __name__ == "__main__":
    main()
