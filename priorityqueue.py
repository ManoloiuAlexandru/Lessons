
class PriorityQueue():
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == []

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        maxel = 0
        for i in range(0, len(self.queue)):
            if self.queue[i] > self.queue[maxel]:
                maxel = i
        item = self.queue[maxel]
        del self.queue[maxel]
        return item


prioq = PriorityQueue()
prioq.insert(1)
prioq.insert(5)
prioq.insert(3)
prioq.insert(4)
print(prioq.delete())
print(prioq.delete())
print(prioq.delete())
print(prioq.delete())
