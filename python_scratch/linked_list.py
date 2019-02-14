class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        past = self.head
        next = self.head.next

        while next is not None:
            past = next
            next = next.next

        past.next = new_node

    def count(self):
        if self.head is None:
            return 0

        count = 1
        next = self.head.next
        while next is not None:
            count += 1
            next = next.next
        return count

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            next_node = self.head
            new_node.next = next_node
            next_node.past = new_node
            self.head = new_node

    def reverse(self):
        previous = None
        current_node = self.head

        while current_node is not None:
            # save a reference to next node
            next_node = current_node.next
            # reverse current pointers
            current_node.past = current_node.next
            current_node.next = previous
            # save previous and point to next node
            previous = current_node
            current_node = next_node

        self.head = previous

    def to_array(self):
        array = []
        node = self.head

        while node.next is not None:
            array.append(node.data)
            node = node.next
        array.append(node.data)

        return array


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.past = None
