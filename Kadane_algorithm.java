
/*
http://en.wikipedia.org/wiki/Kadane%27s_Algorithm
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
https://leetcode.com/problems/maximum-subarray/
 */
import java.util.*;

class Solution {
	public static int maxSubArray(int[] array) {
		int max_so_far = array[0];
		int max_ending_here = 0;

		for (int i = 0; i < array.length; i++) {
			max_ending_here += array[i];
			if (max_so_far < max_ending_here) {
				max_so_far = max_ending_here;
			}
			if (max_ending_here < 0) {
				max_ending_here = 0;
			}
		}
		return max_so_far;
	}

	public static void main(String[] args) {
		int[] my_array = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
		System.out.print(maxSubArray(my_array));
	}
}
