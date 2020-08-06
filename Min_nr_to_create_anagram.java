
/*
Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
 */
import java.util.*;
import java.util.stream.*;

class Solution {
	protected static int count_char(String word, char letter) {
		int nr_of_app = 0;
		for (int i = 0; i < word.length(); i++) {
			if (word.charAt(i) == letter) {
				nr_of_app += 1;
			}
		}
		return nr_of_app;
	}

	public static int minSteps(String s, String t) {
		Map<Character, Integer> s_count = new HashMap<Character, Integer>();
		for (int i = 0; i < s.length(); i++) {
			int count = count_char(s, s.charAt(i));
			s_count.put(s.charAt(i), count);
		}
		Map<Character, Integer> t_count = new HashMap<Character, Integer>();
		for (int i = 0; i < t.length(); i++) {
			int count = count_char(t, t.charAt(i));
			t_count.put(t.charAt(i), count);
		}
		int steps = 0;
		for (Character key : s_count.keySet()) {
			int s_i = 0, s_app, t_app;
			try {
				s_app = s_count.get(key);
			} catch (Exception e) {
				s_app = 0;
			}
			try {
				t_app = t_count.get(key);
			} catch (Exception e) {
				t_app = 0;
			}
			s_i = s_app - t_app;
			if (s_i > 0) {
				steps += s_i;
			}
		}
		return steps;
	}

	public static void main(String[] args) {
		System.out.print(minSteps("anagram","mangaar"));
	}
}
