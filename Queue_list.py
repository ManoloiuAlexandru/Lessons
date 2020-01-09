# https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def enqueue(self, item):
        temp = Node(item)

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


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    print(queue.dequeue())
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(2)
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(2)
    queue.enqueue(2)
    queue.enqueue(2)
    queue.enqueue(2)

    print(queue.dequeue())
