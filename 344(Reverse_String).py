class Solution:
    def reverseString(self, s: list[str]) -> None:
        n=len(s)
        left=0
        right=n-1
        while left<=right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        
class Solution:
    def reverseString(self, s):
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
class Solution:
    def reverseString(self, s):
        s[:] = s[::-1]  # Reverse using slicing and reassign to the same list
