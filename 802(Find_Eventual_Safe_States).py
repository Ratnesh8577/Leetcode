from collections import deque
from typing import List     # for type hinting only

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)

        # -------- 1. Build reversed adjacency list --------
        adj_list = [[] for _ in range(V)]          # reversed graph
        for node in range(V):
            for adjNode in graph[node]:            # original edge node -> adjNode
                adj_list[adjNode].append(node)     # reversed edge adjNode -> node

        # -------- 2. Compute indegree array (original out-degrees) --------
        indegrees = [0] * V
        for node in range(V):
            for adjNode in adj_list[node]:
                indegrees[adjNode] += 1            # edge points *into* adjNode

        # -------- 3. Queue initial safe nodes (terminal nodes) --------
        queue = deque()
        for node in range(V):
            if indegrees[node] == 0:               # no outgoing edges originally
                queue.append(node)

        # -------- 4. BFS to peel off safe layers --------
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)                    # node confirmed safe
            for adjNode in adj_list[node]:         # visit predecessors
                indegrees[adjNode] -= 1            # remove supporting edge
                if indegrees[adjNode] == 0:        # all outgoing paths now safe
                    queue.append(adjNode)

        # -------- 5. Return sorted list of safe nodes --------
        result.sort()
        return result