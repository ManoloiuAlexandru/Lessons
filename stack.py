class myStack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty!")
        return self.data[-1]

    def size(self):
        return len(self.data)

    def show(self):
        return self.data


s = myStack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
