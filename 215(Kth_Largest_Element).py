class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        #  min-heap 
        min_heap = []
        
        
        for num in nums:
            heapq.heappush(min_heap, num)
            #  heap size to k
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        #  heap is the kth largest element
        return min_heap[0]

        