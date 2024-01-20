from static_array import StaticArray


class DynamicArray:
    def __init__(self, size=10):
        # TC : O(N)
        self.size = size
        self.array = StaticArray(size)
        self.current_index = -1

    def append(self, element):
        # TC : O(N)
        if self.array.is_full():
            new_array = StaticArray(2 * self.size)
            for i in range(self.size):
                new_array.insert(self.array.get(i), i)
            self.size = 2 * self.size
            self.current_index += 1
            new_array.insert(element, self.current_index)
            self.array = new_array
        else:
            self.current_index += 1
            self.array.insert(element, self.current_index)

    def insert(self, element, index):
        # TC : O(1)
        self.array.insert(element, index)

    def delete(self, index):
        # TC : O(1)
        self.array.delete(index)

    def get(self, index):
        # TC : O(1)
        return self.array.get(index)

    def clear_array(self):
        # TC : O(N)
        for i in range(self.current_index):
            self.array.insert(None, i)

    def is_full(self):
        # TC : O(1)
        return self.array.is_full()

    def is_empty(self):
        # TC : O(1)
        return self.array.is_empty()

    def fetch_array(self):
        # TC : O(1)
        return self.array.fetch_array()

def main():
    # Example usage of DynamicArray

    # Create an instance of DynamicArray with an initial size of 5
    dynamic_array = DynamicArray(size=5)

    # Append elements to the array
    dynamic_array.append(element="A")
    dynamic_array.append(element="B")
    dynamic_array.append(element="C")

    # Display the current state of the dynamic array
    print("Dynamic Array after initial appends:", dynamic_array.array.fetch_array())

    # Insert an element at a specific index
    dynamic_array.insert(element="X", index=1)

    # Display the array after insertion
    print("Dynamic Array after insertion at index 1:", dynamic_array.array.fetch_array())

    # Delete an element at a specific index
    dynamic_array.delete(index=2)

    # Display the array after deletion
    print("Dynamic Array after deletion at index 2:", dynamic_array.array.fetch_array())

    # Check if the array is full or empty
    print(f"Is the array full? {dynamic_array.is_full()}")
    print(f"Is the array empty? {dynamic_array.is_empty()}")

    # Clear the array
    dynamic_array.clear_array()

    # Display the array after clearing
    print("Dynamic Array after clearing:", dynamic_array.array.fetch_array())

if __name__ == "__main__":
    main()
