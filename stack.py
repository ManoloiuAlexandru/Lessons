"""
https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
"""


# Declaration of class stack
class myStack:

    def __init__(self):
        """
        class constructor
        """
        self.data = []

    def isEmpty(self):
        """
        method that check if the stack is empty
        and returns True if it is empty or False otherwise
        """
        return self.size() == 0

    def push(self, item):
        """
        method that adds an element in the stack
        """
        self.data.append(item)

    def pop(self):
        """
        method that remove and return last item
        """
        return self.data.pop()

    def peek(self):
        """
        method that checks if the stack is empty if not empty return last element
        """
        if self.isEmpty():
            raise Exception("Stack is empty!")
        return self.data[-1]

    def size(self):
        """
        method that returns the length of the stack
        """
        return len(self.data)

    def show(self):
        """
        method that returns the stack
        """
        return self.data


if __name__ == '__main__':
    # Create an object myStack 
    stack = myStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
