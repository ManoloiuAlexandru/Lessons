
/*
Given an integer n, return any array containing n unique integers such that they add up to 0.
https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/ 
 */
import java.util.*;
import java.util.stream.*;

class Solution {
	public static int[] sumZero(int n) {
		List<Integer> final_list = new ArrayList<Integer>();
		for (int i = 0; i < n - 1; i++) {
			final_list.add(i);
		}
		int sum = final_list.stream().mapToInt(Integer::intValue).sum();
		final_list.add(-sum);
		int[] array = new int[final_list.size()];
		for (int i = 0; i < final_list.size(); i++) {
			array[i] = final_list.get(i);
		}
		return array;
	}

	public static void main(String[] args) {
		int[] arr = sumZero(7);
		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i] + " ");
		}
	}
}
