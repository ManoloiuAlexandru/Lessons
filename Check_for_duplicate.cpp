/*
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
https://leetcode.com/problems/contains-duplicate/
The time complexity of this program is: O(n) for the search part
*/
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
bool containsDuplicate(vector<int> nums)
{
	if (nums.size() == 0)
	{
		return false;
	}
	sort(nums.begin(), nums.end());
	for (int i = 0; i < nums.size()-1; i++)
	{
		if (nums[i] == nums[i + 1])
		{
			return true;
		}
	}
	return false;
}
int main()
{
	vector<int> my_array = {};
	cout<<containsDuplicate(my_array);
}
