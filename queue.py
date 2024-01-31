from dynamic_array import DynamicArray

class Queue:
    def __init__(self, size):
        self.array = DynamicArray()
        self.left = 0
        self.right = 0

    def push(self, element):
        self.array.append(element)
        self.right += 1
        return True

    def pop(self):
        if self.left == self.right:
            self.right = 0
            self.left = 0
            return False
        self.array.delete(self.left)
        self.left += 1
        return True

    def fetch_total_elements(self):
        return self.right - self.left

def main():
    # Create a queue with a specified size
    queue_size = 15
    my_queue = Queue(queue_size)

    # Push elements into the queue
    for i in range(1, queue_size + 2):
        if not my_queue.push(i):
            print("Queue is full, cannot push element", i)
        else:
            print("Element", i, "pushed into the queue")

    # Pop elements from the queue
    for _ in range(queue_size + 1):
        if not my_queue.pop():
            print("Queue is empty, cannot pop element")
        else:
            print("Element popped from the queue")

    # Push more elements to see if the queue handles overflow correctly
    for i in range(6, 10):
        if not my_queue.push(i):
            print("Queue is full, cannot push element", i)
        else:
            print("Element", i, "pushed into the queue")

    # Pop elements from the queue
    for _ in range(queue_size):
        if not my_queue.pop():
            print("Queue is empty, cannot pop element")
        else:
            print("Element popped from the queue")

if __name__ == "__main__":
    main()
