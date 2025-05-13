"""class Solution:
    def majorityElement(self, nums):
        counts = {}
        majority = len(nums) // 2

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > majority:
                return num
"""

class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]
