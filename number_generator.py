'''The row defined by the following is considered
recurrence relation:
a) Write only the header of a subprogram sub, which receives through parameter n
a natural number of maximum 8 digits, and which returns the largest term of the string
above smaller or at most equal to n.
Example: if n = 83 then the subprogram will return the value 80. (4p.)
b) Write a program that reads from the keyboard a natural number s (s≤10000000)
and determines a number of distinct numbers whose sum is equal to s, using useful calls
of the subprogram below. The determined numbers will be written on
the first line separated by a space.
Example: if the value read from the keyboard is 63, then the following values, not necessarily in this order: 40 20 3.'''
def f(n):
    if (n <= 5):
        return n
    else:
        return 2 * f(n - 1)


def sub(n):
    nr = 5
    if nr >= n:
        while (f(nr) > n):
            nr -= 1
        return f(nr)
    else:
        while (f(nr) < n):
            nr += 1
        return f(nr - 1)


s = input()
while (s > 0):
    print(sub(s))
    s = s - sub(s)
