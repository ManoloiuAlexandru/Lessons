'''In this py script it is demonstrated how a stack works by implemanting a postfix calculator.
A postfix calculator is a calculator that gets his values like this:
5 2 + which is from 5 + 2
Other example is 5 6 7 * + 1 - which is from 5+6*7-1'''


class myStack:

    def __init__(self):
        self.container = []

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack empty!")
        return self.container[-1]

    def size(self):
        return len(self.container)

    def show(self):
        return self.container


stack = myStack()
result = 0
list_of_tokens = ['5', '6', '7', '*', '+', '1', '-']
for token in list_of_tokens:
    if token.isdigit():
        stack.push(token)
    else:
        if token == '+':
            result = int(stack.pop()) + int(stack.pop())
            stack.push(result)
        elif token == '-':
            result = -(int(stack.pop()) - int(stack.pop()))
            stack.push(result)
        elif token == '*':
            result = int(stack.pop()) * int(stack.pop())
            stack.push(result)
        else:
            result = int(stack.pop()) // int(stack.pop())
            stack.push(result)
print(stack.peek())

