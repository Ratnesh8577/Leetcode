""""from copy import deepcopy
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        visited=[[0 for _ in range(cols)] for _ in range(rows)]
        distance=[[0 for _ in range(cols)] for _ in range(rows)]
        queue=deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    queue.append([r,c,0])
                    visited[r][c]=1
        while len(queue)!=0:
            i,j,d=queue.popleft()
            distance[i][j]=d
            for x,y in [(-1,0),(0,-1),(0,1),(1,0)]:
                new_i,new_j=i+x,j+y
                if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols:
                    continue
                if visited[new_i][new_j]==1:
                    continue
                queue.append([new_i,new_j,d+1])
                visited[new_i][new_j]=1
        return distance

        """
from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dist = [[-1] * cols for _ in range(rows)]
        queue = deque()

        # Add all zero cells to the queue
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))

        # Multi-source BFS
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        return dist
