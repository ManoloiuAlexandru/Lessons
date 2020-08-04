
/*
Write a program that prints on each line the numbers from 1 to n.
But for multiples of three print "Fizz" instead of the number, and for multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
 */
import java.util.*;

class Solution {
	public static void FizzBuzz(int n) {
		for (int i = 0; i <= n; i++) {
			if (i % 15 == 0) {
				System.out.println("FizzBuzz");
			} else if (i % 5 == 0) {
				System.out.println("Buzz");
			} else if (i % 3 == 0) {
				System.out.println("Fizz");
			} else {
				System.out.println(i);
			}
		}
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("n=");
		int n = scanner.nextInt();
		FizzBuzz(n);
	}
}
