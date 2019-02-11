class LinkedList:
    def __init__(self):
        # should the list of 'nodes' just be a node pointing to the next?
        # should I use an array instead?
        self.nodes = None

    def count(self):
        if self.nodes is None:
            return 0

        count = 1
        next = self.nodes.next
        while next is not None:
            count += 1
            next = next.next
        return count

    def insert(self, data):
        new_node = Node(data)

        if self.nodes is None:
            self.nodes = new_node
        else:
            next_node = self.nodes
            new_node.next = next_node
            next_node.previous = new_node
            self.nodes = new_node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # if previous is None, it's the head of the list
        self.previous = None
