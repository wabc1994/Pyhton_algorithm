class stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        return self.items.pop()

    def push(self, element):
        self.items.append(element)

    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
