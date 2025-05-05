"""
class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        temp=[]
        for i in range(n):
            if nums[i]!=0:
                temp.append(nums[i])
        n2=len(temp)
        for i in range (n2):
            nums[i]=temp[i]
        for i in range(n2,n):
            nums[i]=0

        """
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                break
            i += 1
        
        if i == len(nums):
            return
        
        j = i + 1
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
