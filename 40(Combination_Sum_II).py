class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort to handle duplicates
        result = []

        def backtrack(index, total, subset):
            if total == 0:
                result.append(list(subset))
                return
            if total < 0:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates
                subset.append(candidates[i])
                backtrack(i + 1, total - candidates[i], subset)
                subset.pop()

        backtrack(0, target, [])
        return result
