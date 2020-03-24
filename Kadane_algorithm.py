'''http://en.wikipedia.org/wiki/Kadane%27s_Algorithm

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
https://leetcode.com/problems/maximum-subarray/
'''


class Solution:
    def maxSubArray(self, array):
        max_so_far = array[0]
        max_ending_here = 0

        for i in range(0, len(array)):
            max_ending_here += array[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
