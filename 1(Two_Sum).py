class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        hash_map={}
        for i in range(n):
            remaining = target-nums[i]
            if remaining in hash_map:
                return [hash_map [remaining],i]
            hash_map[nums[i]]=i



        """n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
"""

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        