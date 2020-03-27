'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
The solution set must not contain duplicate triplets.

https://leetcode.com/problems/3sum/

Personal note:
This is the naive approach. The time complexity of this program is: O(n^3)
'''
class Solution:
    def threeSum(self, nums):
        nums.sort()
        final_list = []
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if 0 - (nums[i] + nums[j]) in nums[j + 1:]:
                    if sorted([nums[i], nums[j],
                               nums[j + 1:][nums[j + 1:].index(0 - (nums[i] + nums[j]))]]) in final_list:
                        pass
                    else:
                        final_list.append(
                            sorted([nums[i], nums[j], nums[j + 1:][nums[j + 1:].index(0 - (nums[i] + nums[j]))]]))
        return final_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([1, 2, 3, 4]))
