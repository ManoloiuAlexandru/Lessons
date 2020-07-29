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
#include<iostream>
#include<algorithm>
using namespace std;
bool isAnagram(string s, string t)
{
	sort(s.begin(), s.end());
	sort(t.begin(), t.end());
	return s == t;
}
int main()
{
	cout << isAnagram("anagram", "nagaram");
}
