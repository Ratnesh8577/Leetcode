class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        total_subset = 1 << n  # 2^n subsets
        result = []
        for num in range(total_subset):
            subset = []
            for i in range(n):
                if (num & (1 << i)) != 0:
                    subset.append(nums[i])
            result.append(subset)
        return result

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        