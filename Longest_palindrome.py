"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
https://leetcode.com/problems/longest-palindrome/
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict_of_letters = dict()
        max_length = 0
        have_to_add1 = 0
        for i in s:
            dict_of_letters[i] = s.count(i)
        if len(dict_of_letters) == 1:
            return dict_of_letters[s[0]]
        for app in dict_of_letters:
            if dict_of_letters[app] % 2 == 0:
                max_length += dict_of_letters[app]
            elif dict_of_letters[app] % 2 == 1:
                max_length += dict_of_letters[app] - 1
                have_to_add1 = 1
        return max_length + have_to_add1


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome(
        "ababababa"))
