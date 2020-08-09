"""
This problem was from August LeetCoding Challenge day 9.

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.

"""

import copy


class Solution:
    def orangesRotting(self, grid) -> int:
        nr_min = 0
        chanced = 1
        copy_of_grid = copy.deepcopy(grid)
        while chanced != 0:
            chanced = 0
            for col in range(0, len(grid)):
                for line in range(0, len(grid[col])):
                    if grid[col][line] == 2:
                        if line != len(grid[col]) - 1 and grid[col][line + 1] == 1:
                            copy_of_grid[col][line + 1] = 2
                            chanced = 1
                        if line != 0 and grid[col][line - 1] == 1:
                            copy_of_grid[col][line - 1] = 2
                            chanced = 1
                        if col != len(grid) - 1 and grid[col + 1][line] == 1:
                            copy_of_grid[col + 1][line] = 2
                            chanced = 1
                        if col != 0 and grid[col - 1][line] == 1:
                            copy_of_grid[col - 1][line] = 2
                            chanced = 1
            grid = copy.deepcopy(copy_of_grid)
            nr_min += 1
        for col in range(0, len(grid)):
            for line in range(0, len(grid[col])):
                if grid[col][line] == 1:
                    return -1
        nr_min -= 1
        return nr_min


if __name__ == '__main__':
    sol = Solution()
    print(sol.orangesRotting([[2, 1, 0], [1, 1, 0], [0, 1, 1]]))
