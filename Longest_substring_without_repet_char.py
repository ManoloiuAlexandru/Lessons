'''
Given a string, find the length of the longest substring without repeating characters.
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
def lengthOfLongestSubstring(s: str) -> int:
    max_string = ""
    if s == "":
        return 0
    elif len(s) > 1:
        for i in range(0, len(s) - 1):
            string_build = s[i]
            for j in range(i + 1, len(s)):
                if s[j] in string_build:
                    if len(max_string) < len(string_build):
                        max_string = string_build
                    break
                else:
                    string_build += s[j]
            if len(max_string) < len(string_build):
                max_string = string_build
    else:
        return 1

    return len(max_string)


if __name__ == '__main__':
    print(lengthOfLongestSubstring("abacda"))
