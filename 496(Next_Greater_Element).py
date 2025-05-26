"""class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums)
        ans=[-1]*n
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    ans[i]=nums[j]
                    break
        return ans

        
"""
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        # For remaining elements in stack, there is no next greater
        for num in stack:
            next_greater[num] = -1

        return [next_greater[num] for num in nums1]

        