"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
https://leetcode.com/problems/rotate-image/
"""


class Solution:
    def rotate(self, matrix) -> None:
        line_start = 0
        line_end = len(matrix) - 1
        while line_start < line_end:
            aux_first_line = matrix[line_start][line_start:line_end + 1]
            column_nr = list()
            for row in matrix[line_start:line_end + 1]:
                column_nr.append(row[line_start])
            aux_first_column = column_nr
            aux_last_line = matrix[line_end][line_start:line_end + 1]
            column_nr = list()
            for row in matrix[line_start:line_end + 1]:
                column_nr.append(row[line_end])
            aux_last_column = column_nr
            matrix[line_start][line_start:line_end + 1] = aux_first_column[::-1]
            matrix[line_end][line_start:line_end + 1] = aux_last_column[::-1]
            i = 0
            for row in matrix[line_start:line_end + 1]:
                try:
                    row[line_end] = aux_first_line[i]
                    i += 1
                except Exception as e:
                    pass
            i = 0
            for row in matrix[line_start:line_end + 1]:
                try:
                    row[line_start] = aux_last_line[i]
                    i += 1
                except Exception as e:
                    pass
            line_start += 1
            line_end -= 1
        return matrix


if __name__ == '__main__':
    sol = Solution()
    print(sol.rotate([
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]))
