class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        list1 = set()
        for num in nums:
            if num in list1:
                return True
            list1.add(num)
        return False
        