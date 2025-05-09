class StackArray:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, value):
        self.data.append(value)

    def getLastElement(self):
        return self.data[-1] if not self.isEmpty() else None

    def pop(self):
        if not self.isEmpty():
            self.data.pop()
