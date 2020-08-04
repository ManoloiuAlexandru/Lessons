
/*
 Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
https://leetcode.com/problems/contains-duplicate/
 */
import java.util.*;

class Solution {
	public static boolean containsDuplicate(int[] nums)
	{
		Arrays.sort(nums);
		for (int i=0;i<nums.length-1;i++)
		{
			if (nums[i]==nums[i+1])
			{
				return true;
			}
		}
		return false;
	}

	public static void main(String[] args) {
		int[] intArray = new int[]{ 1, 1, 1, 3, 3, 4, 3, 2, 4, 2 }; 
		System.out.print(containsDuplicate(intArray));
	}
}
