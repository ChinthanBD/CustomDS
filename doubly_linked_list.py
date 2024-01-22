from node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None, prev_node=self.head)
        self.head.next_node = self.tail
        self.node_count = 0

    def fetch_head(self):
        return self.head

    def fetch_tail(self):
        # TC : O(1)
        return self.tail

    def add(self, value):
        #TC : O(1)
        if not value:
            return False

        tail = self.fetch_tail()
        new_node = Node(key=None, value=value, next_node=tail, prev_node=tail.prev_node)
        tail.prev_node.next_node = new_node
        tail.prev_node = new_node
        self.node_count += 1
        return True

    def delete(self, value):
        temp = self.fetch_head()
        if not value:
            return False
        while temp:
            if temp.value == value:
                temp.prev_node.next_node = temp.next_node
                temp.next_node.prev_node = temp.prev_node
                self.node_count -= 1
                return True
            temp = temp.next_node
        return False

    def print_doubly_linked_list(self):
        temp = self.fetch_head()
        temp = temp.next_node
        while temp.value:
            print(temp.value, '<->', end='')
            temp = temp.next_node
        print('None')

    def get_position(self, value):
        position = 0
        temp = self.fetch_head()
        while temp:
            position += 1
            if temp.value == value:
                return position
            temp = temp.next_node
        return -1

    def get_element(self, position):
        value = None
        if position > self.node_count or position <= 0:
            return value
        temp = self.fetch_head()
        count = 1
        while temp:
            if position == count:
                return temp.value
            count += 1
            temp = temp.next_node
        return value


def main():
    # Positive Scenario
    dll = DoublyLinkedList()

    # Adding elements
    dll.add(10)
    dll.add(20)
    dll.add(30)

    # Printing the doubly linked list
    print("Doubly Linked List:")
    dll.print_doubly_linked_list()  # Output: 10 <-> 20 <-> 30 <-> None

    # Deleting an element
    deleted_value = 20
    if dll.delete(deleted_value):
        print(f"{deleted_value} deleted successfully.")
    else:
        print(f"{deleted_value} not found in the list.")
    # Output after deletion: 10 <-> 30 <-> None
    print("Doubly Linked List after deletion:")
    dll.print_doubly_linked_list()

    # Getting position of an element
    element_to_find = 30
    position = dll.get_position(element_to_find)
    if position != -1:
        print(f"{element_to_find} found at position {position}.")
    else:
        print(f"{element_to_find} not found in the list.")

    # Getting element at a position
    position_to_get = 2
    value_at_position = dll.get_element(position_to_get)
    if value_at_position is not None:
        print(f"Element at position {position_to_get}: {value_at_position}")
    else:
        print(f"No element found at position {position_to_get}.")

    # Negative Scenario
    # Deleting an element not in the list
    deleted_value_not_in_list = 40
    if dll.delete(deleted_value_not_in_list):
        print(f"{deleted_value_not_in_list} deleted successfully.")
    else:
        print(f"{deleted_value_not_in_list} not found in the list.")

    # Getting position of an element not in the list
    element_to_find_not_in_list = 50
    position_not_in_list = dll.get_position(element_to_find_not_in_list)
    if position_not_in_list != -1:
        print(f"{element_to_find_not_in_list} found at position {position_not_in_list}.")
    else:
        print(f"{element_to_find_not_in_list} not found in the list.")

    # Getting element at an invalid position
    invalid_position = 5
    value_at_invalid_position = dll.get_element(invalid_position)
    if value_at_invalid_position is not None:
        print(f"Element at position {invalid_position}: {value_at_invalid_position}")
    else:
        print(f"No element found at position {invalid_position}.")


if __name__ == "__main__":
    main()
