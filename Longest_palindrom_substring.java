
/*
Given a string s, find the longest palindromic substring in s.
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
https://leetcode.com/problems/longest-palindromic-substring/
 */
import java.util.*;
import java.util.stream.*;

class Solution {
	public static String longestPalindrome(String s) {
		String max_string = "";
		for (int i = 0; i < s.length(); i++) {
			String s1 = extend(s, i, i), s2 = extend(s, i, i + 1);
			if (s1.length() > max_string.length()) {
				max_string = s1;
			}
			if (s2.length() > max_string.length()) {
				max_string = s2;
			}
		}
		return max_string;
	}

	private static String extend(String s, int i, int j) {
		try {
			for (; 0 <= i && j < s.length(); i--, j++) {
				if (s.charAt(i) != s.charAt(j)) {
					break;
				}
			}
		} catch (Exception e) {
			System.out.print(e);
		}
		return s.substring(i + 1, j);
	}

	public static void main(String[] args) {
		System.out.print(longestPalindrome("cbbd"));
	}
}
