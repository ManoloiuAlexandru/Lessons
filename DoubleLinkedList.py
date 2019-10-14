class DoubleNod:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def addnod(self, data):
        if self.head is None:
            self.head = DoubleNod(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            new_nod = DoubleNod(data)
            temp.next = new_nod
            new_nod.back = temp

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def printback(self):
        temp = self.head
        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" ")
            temp = temp.back
