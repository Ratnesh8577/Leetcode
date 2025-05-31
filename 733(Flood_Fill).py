"""class Solution:
    def floodFill(self, image, sr, sc, color):
        def dfs(i, j, new_color, initial_color, vis, r, c):
            if i < 0 or i >= r or j < 0 or j >= c:
                return
            if vis[i][j] != initial_color:
                return
            if vis[i][j] == new_color:
                return
            vis[i][j] = new_color
            dfs(i + 1, j, new_color, initial_color, vis, r, c)
            dfs(i, j - 1, new_color, initial_color, vis, r, c)
            dfs(i - 1, j, new_color, initial_color, vis, r, c)
            dfs(i, j + 1, new_color, initial_color, vis, r, c)

        if image[sr][sc] == color:
            return image

        vis = [row[:] for row in image]  # deep copy
        r, c = len(vis), len(vis[0])
        initial_color = vis[sr][sc]
        dfs(sr, sc, color, initial_color, vis, r, c)
        return vis
"""
"""
class Solution:
    def floodFill(self, image, sr, sc, color):
        original_color = image[sr][sc]
        if original_color == color:
            return image

        m, n = len(image), len(image[0])
        queue = [(sr, sc)]
        image[sr][sc] = color

        while queue:
            i, j = queue.pop(0)
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and image[x][y] == original_color:
                    image[x][y] = color
                    queue.append((x, y))

        return image


"""

class Solution:
    def floodFill(self, image, sr, sc, color):
        original_color = image[sr][sc]
        if original_color == color:
            return image

        m, n = len(image), len(image[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if image[i][j] != original_color:
                return
            image[i][j] = color
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        dfs(sr, sc)
        return image
