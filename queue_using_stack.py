from stack import Stack


class QueueUsingStack:
    def __init__(self):
        self.stack1 = Stack(2)
        self.stack2 = Stack(2)
        self.size = 2

    def push(self, element):
        if self.stack1.fetch_total_elements() == self.size:
            self.size = 2 * self.size
            self.stack2 = Stack(self.size)
            while self.stack1.peek():
                self.stack2.push(self.stack1.pop())
            self.stack1 = Stack(self.size)
            while self.stack2.peek():
                self.stack1.push(self.stack2.pop())
            self.stack2 = Stack(self.size)
        self.stack1.push(element)

    def pop(self):

        stack_size = self.stack1.fetch_total_elements()
        if stack_size == 0:
            return None
        for i in range(stack_size-1):
            self.stack2.push(self.stack1.pop())
        element = self.stack1.pop()

        while self.stack2.peek():
            self.stack1.push(self.stack2.pop())
        return element


def main():
    # Create a queue using stacks
    queue = QueueUsingStack()

    # Push elements into the queue
    queue.push(5)
    queue.push(10)
    queue.push(15)
    queue.push(20)

    # Pop elements from the queue
    print("Popped element:", queue.pop())  # Expect: 5
    print("Popped element:", queue.pop())  # Expect: 10

    # Push more elements into the queue
    queue.push(25)
    queue.push(30)

    # Pop remaining elements from the queue
    print("Popped element:", queue.pop())  # Expect: 15
    print("Popped element:", queue.pop())  # Expect: 20
    print("Popped element:", queue.pop())  # Expect: 25
    print("Popped element:", queue.pop())  # Expect: 30

    # Attempting to pop from an empty queue
    print("Popped element:", queue.pop())  # Expect: None


if __name__ == "__main__":
    main()
