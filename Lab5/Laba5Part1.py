class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class StackLinkedList:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node

    def getLastElement(self):
        return self.top.value if self.top else None

    def pop(self):
        if not self.isEmpty():
            self.top = self.top.next
