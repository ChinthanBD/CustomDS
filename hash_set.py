from dynamic_array import DynamicArray


class HashSet:
    def __init__(self):
        self.hash_set = DynamicArray(11)

    def hashed(self, value):
        # For value range 1-10, your method should return
        # unique value with which we can identify the element
        return value % 100000007

    def add_element(self, element):
        self.hash_set.insert(element, self.hashed(element))

    def delete_element(self, element):
        self.hash_set.delete(self.hashed(element))

    def element_exist(self, element):
        try:
            if self.hash_set.get(self.hashed(element)):
                return True
            return False
        except Exception:
            return False

    def fetch_all(self):
        output = []
        for element in self.hash_set.fetch_array():
            if element:
                output.append(element)
        return output


def main():
    # Example usage of HashSet

    # Create an instance of HashSet
    hash_set = HashSet()

    # Add elements to the HashSet
    hash_set.add_element(element=1)
    hash_set.add_element(element=5)
    hash_set.add_element(element=2)

    # Display the current state of the HashSet
    print("HashSet after adding elements:", hash_set.fetch_all())

    # Check if an element exists in the HashSet
    element_to_check = 15
    if hash_set.element_exist(element=element_to_check):
        print(f"Element {element_to_check} exists in the HashSet.")
    else:
        print(f"Element {element_to_check} does not exist in the HashSet.")

    # Delete an element from the HashSet
    element_to_delete = 5
    hash_set.delete_element(element=element_to_delete)

    # Display the HashSet after deletion
    print("HashSet after deleting element 5:", hash_set.fetch_all())

if __name__ == "__main__":
    main()


