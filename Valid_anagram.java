
/*
Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
https://leetcode.com/problems/valid-anagram/
*/
import java.util.*;

class Solution {
	public static boolean isAnagram(String s, String t) {
		char[] chars = s.toCharArray();
		Arrays.sort(chars);
		s = new String(chars);
		chars = t.toCharArray();
		Arrays.sort(chars);
		t = new String(chars);
		return s.equals(t);
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("s=");
		String s = scanner.next();
		System.out.println("t=");
		String t = scanner.next();
		System.out.print(isAnagram(s, t));
	}
}
