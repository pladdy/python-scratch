class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.items.append(item)

    def peek(self):
        if self.size() > 0:
            return self.items[-1]

    def pop(self):
        if self.size() > 0:
            return self.items.pop()

    def size(self):
        return len(self.items)
