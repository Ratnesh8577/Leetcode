"""class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(g)
        left=0
        right=0
        m = len(s)
        count=0
        g.sort()
        s.sort()
        while left <n and right<m:
            if g[left]<=s[right]:
                count+=1
                left+=1
            right+=1
        return count
"""

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        
        child = 0
        for cookie in s:
            if child < len(g) and g[child] <= cookie:
                child += 1
        return child

