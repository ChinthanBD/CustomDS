from dynamic_array import DynamicArray


class MinHeap:
    def __init__(self):
        self.array = DynamicArray(10)

    def add(self, value):
        self.array.append(value)
        self.heapify_add()

    def delete(self):
        if self.array.is_empty():
            return False

        last_index = self.array.fetch_size() - 1
        self.swap_elements(0, last_index)

        self.array.delete(last_index)
        self.heapify_delete()

        return True

    def heapify_add(self):
        child_index = self.array.fetch_size() - 1

        while child_index > 0:
            parent_index = (child_index - 1) // 2
            child_element = self.array.get(child_index)
            parent_element = self.array.get(parent_index)

            if child_element is not None and parent_element is not None and child_element < parent_element:
                self.swap_elements(parent_index, child_index)

                child_index = parent_index
            else:
                break

    def heapify_delete(self):
        index = 0

        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            min_index = index

            if left_child_index < self.array.fetch_size() and self.array.get(left_child_index) < self.array.get(
                    min_index):
                min_index = left_child_index
            if right_child_index < self.array.fetch_size() and self.array.get(right_child_index) < self.array.get(
                    min_index):
                min_index = right_child_index

            if min_index != index:
                self.swap_elements(index, min_index)
                index = min_index
            else:
                break

    def swap_elements(self, index1, index2):
        element1 = self.array.get(index1)
        element2 = self.array.get(index2)
        self.array.insert(element1, index2)
        self.array.insert(element2, index1)

def main():
    # Create an instance of MinHeap
    min_heap = MinHeap()

    # Add elements to the heap
    min_heap.add(5)
    min_heap.add(3)
    min_heap.add(8)
    min_heap.add(1)
    min_heap.add(7)

    # Display the current state of the heap
    print("Min Heap after adding elements:", min_heap.array.fetch_array())

    # Delete elements from the heap
    deleted = min_heap.delete()
    print(f"Element deleted successfully: {deleted}")
    print("Min Heap after deleting element:", min_heap.array.fetch_array())

    # Try deleting from an empty heap
    deleted = min_heap.delete()
    print(f"Element deleted successfully: {deleted}")
    print("Min Heap after attempting to delete from an empty heap:", min_heap.array.fetch_array())

if __name__ == "__main__":
    main()



