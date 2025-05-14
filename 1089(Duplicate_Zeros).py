class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        n = len(arr)
        zeros = 0
        
        # First pass: Count the number of zeros that would be duplicated
        for i in range(n):
            if arr[i] == 0:
                zeros += 1
        
        # Second pass: Work backwards and shift elements
        for i in range(n - 1, -1, -1):
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0
