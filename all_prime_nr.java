
/*
Given a number n, print all primes smaller than or equal to n.
Example:
Input : n =10
Output : 2 3 5 7
Input : n = 20
Output: 2 3 5 7 11 13 17 19
*/
import java.util.*;

class Solution {
	public static int prime(int number) {
		for (int d = 2; d < number; d++) {
			if (number % d == 0) {
				return 0;
			}
		}
		return 1;
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("n=");
		int n = scanner.nextInt();
		for (int i = 2; i <= n; i++) {
			if (prime(i) == 1) {
				System.out.print(i + " ");
			}
		}
	}
}
