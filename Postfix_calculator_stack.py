'''In this py script it is demontrate how a stack works by implemanting a postfix calculator.
A postfix calculator is a calculator that gates his values like this:
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


s = myStack()
exp = 0
listtoken = ['5', '6', '7', '*', '+', '1', '-']
for token in listtoken:
    if token.isdigit():
        s.push(token)
    else:
        if token == '+':
            exp = int(s.pop()) + int(s.pop())
            s.push(exp)
        elif token == '-':
            exp = -(int(s.pop()) - int(s.pop()))
            s.push(exp)
        elif token == '*':
            exp = int(s.pop()) * int(s.pop())
            s.push(exp)
        else:
            exp = int(s.pop()) // int(s.pop())
            s.push(exp)
print(s.peek())
