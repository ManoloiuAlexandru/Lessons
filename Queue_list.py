class node():
    def __init__(self, data):
        self.data = data
        self.next = None


class queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def enqueue(self, item):
        temp = node(item)

        if self.tail is None:
            self.head = self.tail = temp
            return
        self.tail.next = temp
        self.tail = temp

    def dequeue(self):
        if self.isEmpty():
            return
        temp = self.head
        self.head = temp.next

        if self.head is None:
            self.tail = None
        return str(temp.data)


q = queue()
q.enqueue(1)
print(q.dequeue())
q.enqueue(2)
q.enqueue(3)
q.enqueue(2)
print(q.dequeue())
print(q.dequeue())
q.enqueue(2)
q.enqueue(2)
q.enqueue(2)
q.enqueue(2)

print(q.dequeue())
