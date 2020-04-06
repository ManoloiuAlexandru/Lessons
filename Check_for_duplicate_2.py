'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

https://leetcode.com/problems/contains-duplicate-ii/
The time complexity of this program is: O(n^2)
'''


class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        for i in range(0, len(nums)):
            if nums[i] in nums[i + 1:i + k + 1]:
                for j in range(i + 1, i + k + 1):
                    if j > len(nums):
                        break
                    elif nums[i] == nums[j]:
                        return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))
