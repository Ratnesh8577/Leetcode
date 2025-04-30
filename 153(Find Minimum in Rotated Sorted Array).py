"""class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        mini = float("inf")
        for i in range(n):
            if nums[i]<mini:
                mini = min(mini,nums[i])
        return mini
       """
class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        low= 0
        high=n-1
        mini= float("inf")
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=nums[high]:
                mini=min(mini,nums[mid])
                high=mid-1
            else:
                mini=min(mini,nums[low])
                low=mid+1
        return mini