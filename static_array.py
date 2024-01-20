class StaticArray:
    size: object

    def __init__(self, size):
        # TC: O(N)
        self.size = size
        self.array = [None] * size
        self.occupied_size = 0
        
    def insert(self, element, index):
        # TC: O(1)
        try:
            if type(index) is not int:
                raise TypeError("Type of the index provided is not int")
            if self.size <= index < 0:
                raise IndexError("Given array index is out of range")
            self.array[index] = element
            self.occupied_size += 1

        except Exception as error:
            print(f"Error occurred while inserting the element {element} to array, Error:", str(error))

    def delete(self, index):
        # TC: O(1)
        try:
            if type(index) is not int:
                raise TypeError("Type of the index provided is not int")
            if self.size <= index < 0:
                raise IndexError("Given array index is out of range")

            self.array[index] = None
            self.occupied_size -= 1

        except Exception as error:
            print(f"Error occurred while deleting the element from index:{index} of array, Error:", str(error))

    def get(self, index):
        # TC : O(1)
        try:
            if type(index) is not int:
                raise TypeError("Type of the index provided is not int")
            if self.size <= index < 0:
                raise IndexError("Given array index is out of range")
            return self.array[index]
        except Exception as error:
            print(f"Error while fetching the elements from index {index}, Error:", str(error))
            return None

    def is_empty(self):
        # TC : O(1)
        if self.occupied_size == 0:
            return True
        return False

    def is_full(self):
        # TC : O(1)
        if self.occupied_size == self.size:
            return True
        return False

    def fetch_array(self):
        # TC : O(1)
        return self.array


def main():
    # Example usage of CustomArray

    # Create an instance of CustomArray with a size of 5
    custom_array = StaticArray(size=5)

    # Insert elements into the array
    custom_array.insert(element="A", index=0)
    custom_array.insert(element="B", index=2)
    custom_array.insert(element="C", index=4)

    # Display the current state of the array
    print("Array after insertion:", custom_array.fetch_array())

    # Delete an element from the array
    custom_array.delete(index=2)

    # Display the array after deletion
    print("Array after deletion:", custom_array.fetch_array())

    # Get an element from the array
    index_to_get = 0
    element_at_index = custom_array.get(index=index_to_get)
    if element_at_index is not None:
        print(f"Element at index {index_to_get}: {element_at_index}")

    # Check if the array is empty or full
    print(f"Is the array empty? {custom_array.is_empty()}")
    print(f"Is the array full? {custom_array.is_full()}")


if __name__ == "__main__":
    main()
