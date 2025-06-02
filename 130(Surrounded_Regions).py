from typing import List

class Solution:
    def dfs(self, r, c, visited, rows, cols, board):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if board[r][c] == "X" or visited[r][c]:
            return

        visited[r][c] = 1

        self.dfs(r - 1, c, visited, rows, cols, board)
        self.dfs(r + 1, c, visited, rows, cols, board)
        self.dfs(r, c - 1, visited, rows, cols, board)
        self.dfs(r, c + 1, visited, rows, cols, board)

    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        visited = [[0] * cols for _ in range(rows)]

        # Border DFS
        for c in range(cols):
            if board[0][c] == "O" and not visited[0][c]:
                self.dfs(0, c, visited, rows, cols, board)
            if board[rows - 1][c] == "O" and not visited[rows - 1][c]:
                self.dfs(rows - 1, c, visited, rows, cols, board)

        for r in range(rows):
            if board[r][0] == "O" and not visited[r][0]:
                self.dfs(r, 0, visited, rows, cols, board)
            if board[r][cols - 1] == "O" and not visited[r][cols - 1]:
                self.dfs(r, cols - 1, visited, rows, cols, board)

        # Flip unvisited 'O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and not visited[r][c]:
                    board[r][c] = "X"
