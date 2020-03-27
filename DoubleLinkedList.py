'''https://en.wikipedia.org/wiki/Doubly_linked_list

The time complexity of this program is: O(n)
'''
class DoubleNod:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add_new_nod_to_end(self, data):
        if self.head is None:
            self.head = DoubleNod(data)
        else:
            current_nod = self.head
            while current_nod.next:
                current_nod = current_nod.next
            new_nod = DoubleNod(data)
            current_nod.next = new_nod
            new_nod.back = current_nod

    def print_list_inorder(self):
        current_nod = self.head
        while current_nod:
            print(current_nod.data, end=" ")
            current_nod = current_nod.next

    def print_list_backwards(self):
        current_nod = self.head
        while current_nod.next:
            current_nod = current_nod.next

        while current_nod:
            print(current_nod.data, end=" ")
            current_nod = current_nod.back


if __name__ == '__main__':
    new_list = DoubleLinkedList()
    new_list.add_new_nod_to_end(1)
    new_list.add_new_nod_to_end(2)
    new_list.add_new_nod_to_end(3)
    new_list.print_list_inorder()
    print()
    new_list.print_list_backwards()
