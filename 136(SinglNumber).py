class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        
        # XOR all numbers together
        for num in nums:
            result ^= num
        
        return result
        