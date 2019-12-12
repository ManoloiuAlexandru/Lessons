'''Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.'''
def fibonaci(nr):
    if nr == 1 or nr == 2:
        return 1
    else:
        return fibonaci(nr - 1) + fibonaci(nr - 2)


user_input = int(input("What element from the Fibonacci Sequence you want ?"))
print(fibonaci(user_input))
