'''Given an integer n, return any array containing n unique integers such that they add up to 0.

https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/ 

Personal note:
The time complexity of this program is: O(n)
'''

def sumZero(n: int):
    final_list = []
    for i in range(0, n - 1):
        final_list.append(i)
    final_list.append(-sum(final_list))
    print(final_list)


if __name__ == '__main__':
    sumZero(5)
