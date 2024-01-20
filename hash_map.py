from node import Node
from dynamic_array import DynamicArray
class HashMap:

    def __init__(self):
        self.array = DynamicArray(10)

    def insert(self, key, value):
        element = Node(key, value)
        self.array.insert(element, self.hashed(key))

    def delete(self, key):
        if self.array.get(self.hashed(key)):
            self.array.delete(self.hashed(key))
        else:
            raise KeyError(f"Deletion at {key} is not possible because {key} doesn't exist")

    def get(self, key):
        if self.array.get(self.hashed(key)):
            return self.array.get(self.hashed(key)).value
        else:
            raise KeyError(f"Fetching element with {key} is not possible because {key} doesn't exist")

    def fetch_all(self):
        return [{key : value} for key,value in zip(self.fetch_all_keys(), self.fetch_all_values())]

    def fetch_all_keys(self):
        key_list = []
        for node in self.array.fetch_array():
            if isinstance(node, Node):
                key_list.append(node.key)
        return key_list

    def fetch_all_values(self):
        value_list = []
        for key in self.fetch_all_keys():
            node = self.array.get(self.hashed(key))
            value_list.append(node.value)
        return value_list

    def hashed(self, value):
        # For value range 1-10, your method should return
        # unique value with which we can identify the element
        return value % 100000007


def main():
    # Example usage of HashMap

    # Create an instance of HashMap
    hash_map = HashMap()

    # Insert elements into the HashMap
    hash_map.insert(key=1, value="One")
    hash_map.insert(key=2, value="Eleven")
    hash_map.insert(key=5, value="Twenty-One")

    # Display the current state of the HashMap
    print("HashMap after insertion:", hash_map.fetch_all())

    # Get values from the HashMap
    key_to_get = 1
    try:
        value = hash_map.get(key=key_to_get)
        print(f"Value at key {key_to_get}: {value}")
    except KeyError as e:
        print(str(e))

    # Delete an element from the HashMap
    key_to_delete = 1
    try:
        hash_map.delete(key=key_to_delete)
        print(f"HashMap after deleting key {key_to_delete}:", hash_map.fetch_all())
    except KeyError as e:
        print(str(e))


if __name__ == "__main__":
    main()
