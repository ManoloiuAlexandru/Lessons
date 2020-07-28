"""Given a number n, print all primes smaller than or equal to n.
Example:
Input : n =10
Output : 2 3 5 7
Input : n = 20
Output: 2 3 5 7 11 13 17 19"""


def prime(number):
    for div in range(2, number // 2 + 1):
        if number % div == 0:
            return False
    return True


if __name__ == '__main__':

    given_nr = int(input("What is the number?"))

    for nr in range(2, given_nr):
        if prime(nr) is True:
            print(nr, end=" ")
