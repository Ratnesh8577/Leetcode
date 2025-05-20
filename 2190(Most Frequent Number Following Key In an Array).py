class Solution:
    def mostFrequent(self, nums, key):
        from collections import defaultdict

        count = defaultdict(int)

        for i in range(len(nums) - 1):
            if nums[i] == key:
                count[nums[i + 1]] += 1

        # Return the target with the maximum count
        return max(count, key=count.get)
