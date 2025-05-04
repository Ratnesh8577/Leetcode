class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def solve(start, total, subset):
            if total == n and len(subset) == k:
                result.append(subset[:])
                return
            if total > n or len(subset) > k:
                return
            for i in range(start, 10):
                subset.append(i)
                solve(i + 1, total + i, subset)
                subset.pop()

        solve(1, 0, [])
        return result
