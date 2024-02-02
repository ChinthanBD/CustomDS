from dynamic_array import DynamicArray

class Queue:
    def __init__(self):
        self.array = DynamicArray()
        self.left = 0
        self.right = 0

    def push(self, element):
        # This implementation is wasting storage.
        # IF we push 10 elements, pop 1, inserting another element (ie total size is still 10) makes array size to 20!
        self.array.append(element)
        self.right += 1
        return True

    def pop(self):
        if self.left == self.right:
            self.right = 0
            self.left = 0
            return None
        element = self.array.get(self.left)
        self.array.delete(self.left)
        self.left += 1
        return element

    def fetch_total_elements(self):
        return self.right - self.left


def main():
    queue = Queue()

    # Adding elements to the queue
    queue.push(5)
    queue.push(10)
    queue.push(15)

    # Printing total elements in the queue
    print("Total elements in the queue:", queue.fetch_total_elements())

    # Removing elements from the queue
    print("Popped element:", queue.pop())
    print("Popped element:", queue.pop())

    # Printing total elements in the queue after popping
    print("Total elements in the queue after popping:", queue.fetch_total_elements())


if __name__ == "__main__":
    main()
