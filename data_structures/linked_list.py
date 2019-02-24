class LinkedList:
    """
    Linked list implementation

    TODO: have a linked list class and use it to create single, double, and circular linked list classes...
    """

    def __init__(self):
        """
        Initializes a Doubly Linked list

        Example:
        ```python
            list = LinkedList()
        ```
        """

        self.head = None
        self.count = 0
        """
        The head of the linked list, or first element.
        """

    def append(self, data):
        """
        Given an input, creates a node, and adds to the end of linked list.

        Example:
        ```python
            list = LinkedList()
            list.append("foo")
            # `list` contains a node with a data property set to "foo"
        ```
        """
        new_node = Node(data)
        self.count += 1

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

    def size(self):
        """
        Return the number of nodes in the linked list.

        Example:
        ```python
            list = LinkedList()
            # 3 nodes inserted into list
            print(list.size()) # prints 3 to stdout
        ```
        """
        return self.count
        #
        # if self.head is None:
        #     return count
        #
        # current = self.head
        # while current is not None:
        #     count += 1
        #     current = current.next
        # return count

    def delete(self, data):
        """
        Traverse list looking for `data`; if a node's data matches the input it's deleted.
        All matching nodes are deleted.

        Example:
        ```python
            list = LinkedList()
            # nodes are inserted and the list, as an array, is [1, 2, 3, 3, 4, 5]
            list.delete(3)
            # list as an array will now be [1, 2, 4, 5]
        ```
        """
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
                self.count -= 1
            else:
                last_node = current_node
            current_node = current_node.next

    def insert(self, data):
        """
        Given an input, create a node, and insert into the head of the list.

        Example:
        ```python
            list = LinkedList()
            list.insert("foo")
            # `list` contains a node with a data property set to "foo"
        ```
        """
        new_node = Node(data)
        self.count += 1

        if self.head is None:
            self.head = new_node
        else:
            next_node = self.head
            self.head = new_node
            self.head.next = next_node
            next_node.past = new_node

    def reverse(self):
        """
        Reverse the order of the list.

        Example:
        ```python
            # given a list, as an array, looks like [1, 2, 3, 4, 5]
            list.reverse()
            # list will now, as an array, look like [5, 4, 3, 2, 1]
        ```
        """
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
        """
        Returns the linked list as an array of the data properties of each node.

        Example:
        ```python
            # given a list with 3 nodes with data 1, 2, 3
            print(list.to_array())
            # will print '[1, 2, 3]'
        ```
        """
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
        """
        Given an input, creates a new node, to be used in a linked list.
        """

        self.data = data
        """
        The data the node is storing.
        """

        self.next = None
        """
        Pointer to the next node in the list.
        """

        self.past = None
        """
        Pointer to the previous node in the list.
        """

    def to_string(self):
        """
        Return a node as a string with each property on a newline.
        """
        strs = ["Node ID: {}".format(self)]
        strs.append("Node data: {}".format(self.data))
        strs.append("Node next: {}".format(self.next))
        strs.append("Node past: {}".format(self.past))
        return "\n".join(strs)
