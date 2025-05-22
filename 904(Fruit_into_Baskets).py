"""class Solution:
    def totalFruit(self, fruits):
        max_length = 0
        n = len(fruits)
        for i in range(n):
            my_set = set()
            for j in range(i, n):
                my_set.add(fruits[j])
                if len(my_set) > 2:
                    break
                max_length = max(max_length, j - i + 1)
        return max_length
"""
class Solution:
    def totalFruit(self, fruits):
        max_length = 0
        n = len(fruits)
        my_dict = {}
        left = 0

        for right in range(n):
            my_dict[fruits[right]] = my_dict.get(fruits[right], 0) + 1

            while len(my_dict) > 2:
                my_dict[fruits[left]] -= 1
                if my_dict[fruits[left]] == 0:
                    del my_dict[fruits[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
