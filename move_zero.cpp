/*
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
(https://leetcode.com/problems/move-zeroes/)
*/
#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
	void moveZeroes(vector<int>& nums) {
		int j = 0;
		for (int i = 0; i < nums.size(); i++) {
			if (nums[i] != 0)
			{
				nums[j] = nums[i];
				j += 1;
			}
		}
		for (j; j < nums.size(); j++) {
			nums[j] = 0;
		}
	}
	void print_vector(vector<int>nums)
	{
		int i;
		for (i = 0; i < nums.size(); i++)
		{
			cout << nums[i] << " ";
		}
	}
};
int main()
{
	Solution sol;
	vector<int> nums = { 1,2,3 };
	sol.moveZeroes(nums);
	sol.print_vector(nums);
}
