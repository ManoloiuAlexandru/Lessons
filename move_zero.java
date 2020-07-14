
/*Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
(https://leetcode.com/problems/move-zeroes/)*/
import java.util.*;

class Solution {
	public static int[] moveZeroes(int[] nums) {
		int poz_of_zero = 0;

		for (int i = 0; i < nums.length; ++i) {
			if (nums[i] != 0) {
				int aux = nums[poz_of_zero];
				nums[poz_of_zero] = nums[i];
				poz_of_zero += 1;
				nums[i] = aux;
			}
		}
		return nums;
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("n=");
		Integer n = scanner.nextInt();
		int[] list_of_nr = new int[n];
		for (int i = 0; i < n; i++) {
			System.out.println("Element=");
			list_of_nr[i] = scanner.nextInt();
		}
		list_of_nr = moveZeroes(list_of_nr);
		for (int i = 0; i < list_of_nr.length; i++) {
			System.out.print(list_of_nr[i] + " ");
		}
	}
}
