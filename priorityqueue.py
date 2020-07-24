"""
https://www.geeksforgeeks.org/priority-queue-set-1-introduction/
"""


# Declaration of class PriorityQueue
class PriorityQueue:

    def __init__(self):
        """
        class constructor
        """
        self.queue = []

    def isEmpty(self):
        """
        method that checks if the queue is empty and returns True if it is empty or False otherwise
        """
        return len(self.queue) == []

    def insert(self, data):
        """
        method that adds new data to the queue
        """
        self.queue.append(data)

    def delete(self):
        """
        method that deletes the max element(the element with the highest priority) from the list
        """
        maxel = 0
        for i in range(0, len(self.queue)):
            if self.queue[i] > self.queue[maxel]:
                maxel = i
        item = self.queue[maxel]
        del self.queue[maxel]
        return item


if __name__ == '__main__':
    prioq = PriorityQueue()
    prioq.insert(1)
    prioq.insert(5)
    prioq.insert(3)
    prioq.insert(4)
    print(prioq.delete())
    print(prioq.delete())
    print(prioq.delete())
    print(prioq.isEmpty())
    print(prioq.delete())
