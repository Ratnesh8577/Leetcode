class Solution(object):
    def searchRange(self, nums, target):
        first=-1
        last=-1
        n=len(nums)
        for i in range(n):
            if nums[i]==target:
                if first==-1:
                    first=i
                last=i
        return [first,last]

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        