class Solution:
    def sortArray(self, nums):
        def heapify(i, n):
            while True:
                largest = i
                l, r = 2*i + 1, 2*i + 2
                if l < n and nums[l] > nums[largest]: largest = l
                if r < n and nums[r] > nums[largest]: largest = r
                if largest == i: break
                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest

        n = len(nums)
        for i in range(n//2 - 1, -1, -1): heapify(i, n)
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(0, i)
        return nums
