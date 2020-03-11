'''Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
https://leetcode.com/problems/valid-anagram/
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if ''.join(sorted(s)) == ''.join(sorted(t)):
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))
