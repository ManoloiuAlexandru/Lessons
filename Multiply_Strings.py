"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
https://leetcode.com/problems/multiply-strings/
"""


class Solution:

    # Solution using the function int()
    # def multiply(self, num1: str, num2: str) -> str:
    #     return str(int(num1) * int(num2))

    # Solution with no function int()
    def multiply(self, num1: str, num2: str) -> str:
        value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        num1_nr = 0
        num2_nr = 0
        for i in num1:
            num1_nr = num1_nr * 10 + value[i]
        for i in num2:
            num2_nr = num2_nr * 10 + value[i]
        return str(num1_nr * num2_nr)


if __name__ == '__main__':
    sol = Solution()
    print(sol.multiply("2", "3"))
