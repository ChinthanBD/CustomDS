class StaticArray:
    size: object

    def __init__(self, size):
        # TC: O(N)
        self.size = size
        self.array = [None] * size
        self.occupied_size = 0
        self.min_element = 9999999
        self.max_element = -9999999
        
    def insert(self, element, index):
        # TC: O(1)
        try:

            if type(index) is not int:
                raise TypeError("Type of the index provided is not int")
            if self.size <= index < 0:
                raise IndexError("Given array index is out of range")
            if self.array[index] is None:
                self.occupied_size += 1
            self.array[index] = element
            if element:
                self.min_element = min(self.min_element, element)
                self.max_element = max(self.max_element, element)

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

    def get_min_value(self):
        # TC : O(1)
        if self.occupied_size == 0:
            return None
        return self.min_element

    def get_max_value(self):
        # TC : O(1)
        if self.occupied_size == 0:
            return None
        return self.max_element

    def get_occurance_of_value(self, value):
        # TC : O(N)
        element_occurance_count = 0
        for element in self.array:
            if element == value:
                element_occurance_count += 1
        return element_occurance_count

    def fetch_size(self):
        return self.occupied_size


def main():
    # Example usage of StaticArray

    # Create an instance of StaticArray with an initial size of 5
    static_array = StaticArray(size=5)

    # Insert elements into the array
    static_array.insert(element=10, index=0)
    static_array.insert(element=20, index=1)
    static_array.insert(element=30, index=2)

    # Display the current state of the array
    print("Array after insertion:", static_array.fetch_array())

    # Check if the array is empty or full
    print(f"Is the array empty? {static_array.is_empty()}")
    print(f"Is the array full? {static_array.is_full()}")

    # Fetch the minimum and maximum values
    print(f"Minimum value in the array: {static_array.get_min_value()}")
    print(f"Maximum value in the array: {static_array.get_max_value()}")

    # Get the occurrence of a specific value
    value_to_check = 20
    occurrence_count = static_array.get_occurance_of_value(value_to_check)
    print(f"Occurrence count of {value_to_check}: {occurrence_count}")

    # Delete an element from the array
    index_to_delete = 1
    static_array.delete(index=index_to_delete)

    # Display the array after deletion
    print(f"Array after deleting element at index {index_to_delete}:", static_array.fetch_array())

if __name__ == "__main__":
    main()

