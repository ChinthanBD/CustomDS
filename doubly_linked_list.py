from node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def fetch_head(self):
        return self.head

    def fetch_tail(self):
        temp = self.head
        while temp.next_node:
            temp = temp.next_node
        return temp

    def insert_node(self, value):
        if self.head is None:
            self.head = Node(key=None, value=value, next_node=None, prev_node=None)
        else:
            tail = self.fetch_tail()
            tail.next_node = Node(key=None, value=value, next_node=None, prev_node=tail)
        return self.head

    def delete_node(self, value):
        temp = self.fetch_head()
        while temp.next_node and temp:
            if temp.value == value:
                temp.prev_node.next_node = temp.next_node
                temp.next_node.prev_node = temp.prev_node
                break
            temp = temp.next_node
        return self.fetch_head()

    def print_doubly_linked_list(self):
        temp = self.fetch_head()
        while temp:
            print(temp.value, '<->', end='')
            temp = temp.next_node
        print('None')

def main():
    # Creating a Doubly Linked List
    doubly_linked_list = DoublyLinkedList()

    # Inserting nodes into the linked list
    doubly_linked_list.insert_node(10)
    doubly_linked_list.insert_node(20)
    doubly_linked_list.insert_node(30)

    # Displaying the initial state of the linked list
    print("Doubly Linked List:")
    doubly_linked_list.print_doubly_linked_list()

    # Deleting a node from the linked list
    value_to_delete = 20
    doubly_linked_list.delete_node(value_to_delete)

    # Displaying the linked list after deletion
    print(f"\nDoubly Linked List after deleting node with value {value_to_delete}:")
    doubly_linked_list.print_doubly_linked_list()


if __name__ == "__main__":
    main()
