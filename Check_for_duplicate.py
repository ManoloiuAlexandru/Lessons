'''Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
https://leetcode.com/problems/contains-duplicate/

The time complexity of this program is: O(n)
'''


class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
