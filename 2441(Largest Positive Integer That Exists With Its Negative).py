"""class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_k = -1

        for num in nums:
            if -num in num_set:
                max_k = max(max_k, abs(num))

        return max_k

   """    

class Solution:
    def findMaxK(self, nums):
        nums.sort()
        left, right = 0, len(nums) - 1
        
        while left < right:
            total = nums[left] + nums[right]
            if total == 0:
                return nums[right]
            elif total > 0:
                right -= 1
            else:
                left += 1
        
        return -1
 