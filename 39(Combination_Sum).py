class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(index, subset, total):
            if total == target:
                result.append(list(subset))
                return
            if total > target or index >= len(candidates):
                return

            # Include the current number
            subset.append(candidates[index])
            backtrack(index, subset, total + candidates[index])
            subset.pop()

            # Exclude the current number and move to the next
            backtrack(index + 1, subset, total)

        backtrack(0, [], 0)
        return result
