from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        first_positive = bisect_right(nums, 0)
        first_zero = bisect_left(nums, 0)
        pos = len(nums) - first_positive
        neg = first_zero
        return max(pos, neg)
