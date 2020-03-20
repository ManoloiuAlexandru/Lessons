'''
Given a string s, find the longest palindromic substring in s.
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
https://leetcode.com/problems/longest-palindromic-substring/
'''


def longestPalindrome(s: str) -> str:
    if s == "":
        return ""
    else:
        max_string = ""
        for i in range(0, len(s) - 1):
            for j in range(len(s), i + 1, -1):
                if s[i:j] == s[i:j][::-1]:
                    if len(max_string) < len(s[i:j]):
                        max_string = s[i:j]
        if max_string == "":
            max_string = s[0]
        return max_string


if __name__ == '__main__':
    print(longestPalindrome("abacda"))
