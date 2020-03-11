'''Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.



Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
'''


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = dict()
        for char in set(s):
            s_count[char] = s.count(char)
        t_count = dict()
        for char in set(t):
            t_count[char] = t.count(char)
        steps = 0
        for i in s_count:
            s_i = s_count.get(i, 0) - t_count.get(i, 0)
            if s_i > 0:
                steps += s_i
        return steps


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSteps("leetcode", "practice"))
