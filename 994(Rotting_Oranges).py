"""class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = []
        fresh = 0

        # Add all rotten oranges to the queue and count fresh ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, time)
                elif grid[i][j] == 1:
                    fresh += 1

        time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS to rot adjacent fresh oranges
        while queue:
            i, j, minute = queue.pop(0)
            time = max(time, minute)
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    fresh -= 1
                    queue.append((x, y, minute + 1))

        return time if fresh == 0 else -1
"""
from typing import List
from collections import deque
import copy

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        grid_copy = copy.deepcopy(grid)
        fresh_cnt = 0
        queue = deque()

        # Initialize queue with rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid_copy[r][c] == 2:
                    queue.append((r, c))
                elif grid_copy[r][c] == 1:
                    fresh_cnt += 1

        minutes = 0
        while queue and fresh_cnt > 0:
            minutes += 1
            total_rotten = len(queue)
            for _ in range(total_rotten):
                i, j = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_i, new_j = i + dx, j + dy
                    if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                        continue
                    if grid_copy[new_i][new_j] != 1:
                        continue
                    fresh_cnt -= 1
                    grid_copy[new_i][new_j] = 2
                    queue.append((new_i, new_j))

        return minutes if fresh_cnt == 0 else -1
