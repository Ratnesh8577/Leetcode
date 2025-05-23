class Solution:
    def countNegatives(self, grid):
        m, n = len(grid), len(grid[0])
        row, col = 0, n - 1
        count = 0

        while row < m and col >= 0:
            if grid[row][col] < 0:
                count += m - row
                col -= 1
            else:
                row += 1

        return count
