class Solution:
    def dfs(self, current_Node, visited, graph, color):
        visited[current_Node] = color
        for adjNode in graph[current_Node]:
            if visited[adjNode] != -1:
                if visited[adjNode] == color:
                    return False
            else:
                if color == 0:
                    ans = self.dfs(adjNode, visited, graph, 1)
                else:
                    ans = self.dfs(adjNode, visited, graph, 0)
                if ans == False:
                    return False
        return True   # ✅ Fix: Correct return statement here

    def isBipartite(self, graph: List[List[int]]) -> bool:
        total_node = len(graph)
        visited = [-1] * total_node
        for index in range(0, total_node):
            if visited[index] == -1:
                ans = self.dfs(index, visited, graph, 0)
                if ans == False:
                    return False
        return True
