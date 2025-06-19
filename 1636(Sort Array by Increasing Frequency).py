class Solution:
    def frequencySort(self, nums):
        # Step 1: Build frequency dictionary manually
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 2: Define custom comparison using a key function class
        class SortKey:
            def __init__(self, value):
                self.value = value

            def __lt__(self, other):
                if freq[self.value] != freq[other.value]:
                    return freq[self.value] < freq[other.value]  # Lower frequency first
                else:
                    return self.value > other.value  # Higher value first if same frequency

        # Step 3: Sort using the custom key wrapper
        nums.sort(key=SortKey)
        return nums
