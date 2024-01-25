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

    def get_min_value(self):
        # TC : O(1)
        self.array.get_min_value()

    def get_max_value(self):
        # TC : O(1)
        return self.array.get_max_value()

    def get_occurance_of_value(self, value):
        # TC : O(N)
        return self.array.get_occurance_of_value(value)

    def fetch_size(self):
        return self.array.fetch_size()

def main():
    # Example usage of DynamicArray

    # Create an instance of DynamicArray with an initial size of 5
    dynamic_array = DynamicArray(size=5)

    # Append elements to the array
    dynamic_array.append(element=10)
    dynamic_array.append(element=20)
    dynamic_array.append(element=30)

    # Display the current state of the array
    print("Array after appending elements:", dynamic_array.fetch_array())

    # Check if the array is empty or full
    print(f"Is the array empty? {dynamic_array.is_empty()}")
    print(f"Is the array full? {dynamic_array.is_full()}")

    # Fetch the minimum and maximum values
    print(f"Minimum value in the array: {dynamic_array.get_min_value()}")
    print(f"Maximum value in the array: {dynamic_array.get_max_value()}")

    # Get the occurrence of a specific value
    value_to_check = 20
    occurrence_count = dynamic_array.get_occurance_of_value(value_to_check)
    print(f"Occurrence count of {value_to_check}: {occurrence_count}")

    # Insert an element at a specific index
    index_to_insert = 1
    dynamic_array.insert(element=15, index=index_to_insert)

    # Display the array after insertion
    print(f"Array after inserting element at index {index_to_insert}:", dynamic_array.fetch_array())

    # Delete an element from the array
    index_to_delete = 2
    dynamic_array.delete(index=index_to_delete)

    # Display the array after deletion
    print(f"Array after deleting element at index {index_to_delete}:", dynamic_array.fetch_array())

    # Clear the array
    dynamic_array.clear_array()

    # Display the array after clearing
    print("Array after clearing:", dynamic_array.fetch_array())


if __name__ == "__main__":
    main()
