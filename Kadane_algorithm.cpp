/*
http://en.wikipedia.org/wiki/Kadane%27s_Algorithm
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
https://leetcode.com/problems/maximum-subarray/
*/
#include<iostream>
#include<vector>
using namespace std;
int maxSubArray(vector<int>& nums) 
{
    int max_so_far = nums[0];
    int max_ending_here = 0;

    for (int i = 0; i < nums.size(); i++)
    {
        max_ending_here += nums[i];
        if (max_so_far < max_ending_here)
        {
            max_so_far = max_ending_here;
        }
        if (max_ending_here < 0)
        {
            max_ending_here = 0;
        }
    }
    return max_so_far;
}
int main()
{
    vector<int> myarray = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
    cout<<maxSubArray(myarray);
}
