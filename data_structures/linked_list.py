class LinkedList:
    """ Linked list implementation
        TODO: have a linked list class and use it to create single, double, and circular linked list classes...
    """

    def __init__(self):
        self.head = None

    def append(self, data):
        """ append data as a node to the linked list.  has to traverse the list """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        past_node = None
        while current_node is not None:
            past_node = current_node
            current_node = current_node.next

        past_node.next = new_node
        new_node.past = past_node

    def count(self):
        count = 0

        if self.head is None:
            return count

        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def delete(self, data):
        """ traverse list and if data is found delete that node from list """
        current_node = self.head
        last_node = None
        while current_node is not None:
            if current_node.data == data:
                if current_node == self.head:
                    self.head = current_node.next
                else:
                    last_node.next = current_node.next
                    if current_node.next is not None:
                        current_node.next.past = last_node
            else:
                last_node = current_node
            current_node = current_node.next

    def insert(self, data):
        """ inserts a new node of data as the head of the list """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            next_node = self.head
            self.head = new_node
            self.head.next = next_node
            next_node.past = new_node

    def reverse(self):
        """ reverse the linked list with one pass by swapping each next/past references """
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
        """ return an array of each nodes 'data' property """
        array = []
        node = self.head

        if node is None:
            return array

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

    def to_string(self):
        """ convert node to string for printing """
        strs = ["Node ID: {}".format(self)]
        strs.append("Node data: {}".format(self.data))
        strs.append("Node next: {}".format(self.next))
        strs.append("Node past: {}".format(self.past))
        return "\n".join(strs)
