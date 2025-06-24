class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        freq = [0] * (n * n + 1)
        
        # Flatten grid and count frequencies
        for row in grid:
            for num in row:
                freq[num] += 1

        repeated = missing = -1
        for num in range(1, n * n + 1):
            if freq[num] == 2:
                repeated = num
            elif freq[num] == 0:
                missing = num
        
        return [repeated, missing]
