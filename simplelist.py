class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist():
    def __init__(self):
        self.head = None

    def insertlast(self, new_data):
        if self.head is None:
            new_nod = node(new_data)
            self.head = new_nod
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            new_nod = node(new_data)
            temp.next = new_nod

    def insertinlist(self, new_data):
        temp = self.head
        if temp is None:
            print("The list is empty")
        while temp.data != new_data and temp.next is not None:
            temp = temp.next
        if temp.data == new_data:
            new_nod = node(new_data)
            new_nod.next = temp.next
            temp.next = new_nod
        else:
            self.insertlast(new_data)

    def printlist(self):
        count = 0
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            count += 1
        print("Number of elements in list:", count)


def reverseList(list):
    new_list = linkedlist()
    while list:
        if new_list.head is None:
            new_node = node(list.data)
            new_list.head = new_node
        else:
            new_node = node(list.data)
            copy_list = new_list.head
            new_list.head = new_node
            new_list.head.next = copy_list
        list = list.next
    return new_list


if __name__ == '__main__':
    linklist = linkedlist()

    linklist.insertlast(1)
    linklist.insertlast(2)
    linklist.insertlast(3)
    linklist.insertlast(4)
    linklist.insertlast(5)
    linklist.insertinlist(4)
    linklist.insertinlist(6)
    revlist = reverseList(linklist.head)
    revlist.printlist()
    linklist.printlist()
