import sys
import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        # 1. distance grid: best effort seen so far for every cell
        effort_arr = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        effort_arr[0][0] = 0

        # 2. min-heap with tuples (effort, row, col)
        priority_queue = [[0, 0, 0]]

        while priority_queue:
            eff, i, j = heapq.heappop(priority_queue)

            # 3. goal reached – current effort is already minimal
            if i == rows - 1 and j == cols - 1:
                return eff

            # 4. explore four neighbours
            for x, y in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                new_i, new_j = i + x, j + y
                # skip when out of bounds
                if new_i < 0 or new_j < 0 or new_i >= rows or new_j >= cols:
                    continue

                # effort of stepping into neighbour
                step_gap = abs(heights[new_i][new_j] - heights[i][j])
                new_eff  = max(eff, step_gap)

                # 5. relax if we found a gentler path
                if new_eff < effort_arr[new_i][new_j]:
                    effort_arr[new_i][new_j] = new_eff
                    heapq.heappush(priority_queue, [new_eff, new_i, new_j])