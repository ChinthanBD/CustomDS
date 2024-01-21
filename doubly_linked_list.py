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

        head = self.fetch_head()
        tail = self.fetch_tail()

        if self.node_count == 0:
            new_node = Node(key=None, value=value, next_node=None, prev_node=None)
            new_node.next_node = head.next_node
            new_node.prev_node = head.next_node.prev_node
            head.next_node = new_node
            tail.prev_node = new_node

            self.node_count += 1
            return True
        else:
            new_node = Node(key=None, value=value, next_node=None, prev_node=tail)

            new_node.prev_node = tail.prev_node
            tail.prev_node.next_node = new_node
            new_node.next_node = tail
            tail.prev_node = new_node
            self.node_count += 1
            return True

    def delete(self, value):
        temp = self.fetch_head()
        #[1]
        while temp:
            if temp.value == value:
                if temp.prev_node:
                    temp.prev_node.next_node = temp.next_node
                if temp.next_node:
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
    # Creating a Doubly Linked List
    doubly_linked_list = DoublyLinkedList()

    # Inserting nodes into the linked list
    doubly_linked_list.add(10)
    doubly_linked_list.add(20)
    doubly_linked_list.add(30)

    # Displaying the initial state of the linked list
    print("Doubly Linked List:")
    doubly_linked_list.print_doubly_linked_list()

    # Deleting a node from the linked list
    value_to_delete = 20
    doubly_linked_list.delete(value_to_delete)

    # Displaying the linked list after deletion
    print(f"\nDoubly Linked List after deleting node with value {value_to_delete}:")
    doubly_linked_list.print_doubly_linked_list()


if __name__ == "__main__":
    main()
