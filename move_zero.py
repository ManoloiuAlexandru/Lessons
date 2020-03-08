'''Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
(https://leetcode.com/problems/move-zeroes/)'''


def move_zeros(nums):
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == 0:
            nums.append(0)
            nums.remove(0)
        i += 1
    return nums


if __name__ == '__main__':
    print(move_zeros([0, 1, 0, 3, 12]))
