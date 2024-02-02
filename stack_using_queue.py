from queue import Queue


class StackUsingQueue:
    def __init__(self, size):
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.size = size

    def push(self, element):
        if self.queue1.fetch_total_elements() <= self.size:
            self.queue1.push(element)
            return True
        return False

    def pop(self):
        if self.queue1.fetch_total_elements() == 0:
            return None
        for i in range(self.queue1.fetch_total_elements()-1):
            self.queue2.push(self.queue1.pop())
        element = self.queue1.pop()
        self.queue1 = self.queue2
        self.queue2 = Queue()
        return element


def main():
    stack = StackUsingQueue(5)

    # Adding elements to the stack
    stack.push(5)
    stack.push(10)
    stack.push(15)

    # Removing elements from the stack
    print("Popped element:", stack.pop())
    print("Popped element:", stack.pop())


if __name__ == "__main__":
    main()






