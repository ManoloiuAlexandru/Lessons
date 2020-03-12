'''
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?
https://leetcode.com/problems/max-increase-to-keep-city-skyline/
'''
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        sums = 0
        max_bottom_top = list()
        max_left_right = list()
        for line in grid:
            max_left_right.append(max(line))
        for line in range(0, len(grid)):
            maxim = -1
            for column in range(0, len(grid[line])):
                if maxim < grid[column][line]:
                    maxim = grid[column][line]
            max_bottom_top.append(maxim)
        new_grid = list()
        for line in grid:
            new_grid.append(max_bottom_top)
        left_right_poz = 0
        final_grid = list()
        for line in new_grid:
            new_line = list()
            for column in line:
                if max_left_right[left_right_poz] > column:
                    new_line.append(column)
                else:
                    new_line.append(max_left_right[left_right_poz])
            final_grid.append(new_line)
            left_right_poz += 1
        sumi, sumf = 0, 0
        for line in final_grid:
            sumf += (sum(line))
        for line in grid:
            sumi += sum(line)
        return sumf - sumi


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
