from doubly_linked_list import DoublyLinkedList


class SinglyLinkedList:
    def __init__(self):
        self.head = DoublyLinkedList()

    def fetch_head(self):
        return self.head.fetch_head()

    def fetch_tail(self):
        return self.head.fetch_tail()

    def add_node(self, value):
        return self.head.add_node(value)

    def delete_node(self, value):
        return self.head.delete_node(value)

    def print_singly_linked_list(self):
        temp = self.fetch_head()
        while temp:
            print(temp.value, '->', end='')
            temp = temp.next_node
        print('None')


def main():
    # Creating a Singly Linked List
    singly_linked_list = SinglyLinkedList()

    # Adding nodes to the linked list
    singly_linked_list.add_node(10)
    singly_linked_list.add_node(20)
    singly_linked_list.add_node(30)

    # Displaying the initial state of the linked list
    print("Singly Linked List:")
    singly_linked_list.print_singly_linked_list()

    # Deleting a node from the linked list
    value_to_delete = 20
    singly_linked_list.delete_node(value_to_delete)

    # Displaying the linked list after deletion
    print(f"\nSingly Linked List after deleting node with value {value_to_delete}:")
    singly_linked_list.print_singly_linked_list()


if __name__ == "__main__":
    main()
