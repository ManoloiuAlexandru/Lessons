"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.

https://leetcode.com/problems/valid-sudoku/
"""


class Solution:
    def isValidSudoku(self, board) -> bool:
        for row in board:
            for number in row:
                if number != "." and row.count(number) > 1:
                    return False
        for column in range(0, len(board)):
            column_nr = list()
            for row in board:
                column_nr.append(row[column])
            for number in column_nr:
                if number != "." and column_nr.count(number) > 1:
                    return False
        matrix_3x9 = list()
        for column in range(0, len(board), 3):
            matrix_3x9.append(board[0 + column])
            matrix_3x9.append(board[1 + column])
            matrix_3x9.append(board[2 + column])
            matrix_3x3 = list()
            i = 27
            while i > 0:
                for j in range(0, 3):
                    for t in range(0, 3):
                        matrix_3x3.append(matrix_3x9[t][0])
                        del matrix_3x9[t][0]
                for number in matrix_3x3:
                    if number != "." and matrix_3x3.count(number) > 1:
                        return False
                matrix_3x3.clear()
                i -= 9
            matrix_3x9.clear()
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValidSudoku([
        ["9", "5", "7", "6", "1", "3", "2", "8", "4"],
        ["4", "8", "3", "2", "5", "7", "1", "9", "6"],
        ["6", "1", "2", "8", "4", "9", "5", "3", "7"],
        ["1", "7", "8", "3", "6", "4", "9", "5", "2"],
        ["5", "2", "4", "9", "7", "1", "3", "6", "8"],
        ["3", "6", "9", "5", "2", "8", "7", "4", "1"],
        ["8", "4", "5", "7", "9", "2", "6", "1", "3"],
        ["2", "9", "1", "4", "3", "6", "8", "7", "5"],
        ["7", "3", "6", "1", "8", "5", "4", "2", "9"]
    ]))
