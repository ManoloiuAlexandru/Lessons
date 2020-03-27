'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
http://leetcode.com/problems/pascals-triangle/

Personal note:
The time complexity of this program is: O(n^2)
'''
class Solution:
    def generate(self, numRows: int):
        final_list = []
        if numRows==0:
            return final_list
        elif numRows==1:
            return [[1]]
        else:
            first_list = [1]
            second_list = [1, 1]
            final_list.append(first_list)
            final_list.append(second_list)
            for i in range(2, numRows):
                first_list = second_list
                second_list = [1]
                for j in range(0, len(first_list) - 1):
                    second_list.append(first_list[j] + first_list[j + 1])
                second_list.append(1)
                final_list.append(second_list)
            return final_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(5))
