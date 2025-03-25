class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Use XOR to find the added character
        result = 0
        
        # XOR all characters in s and t
        for char in s:
            result ^= ord(char)
        
        for char in t:
            result ^= ord(char)
        
        # Result will hold the ASCII value of the added character
        return chr(result)



'''
XOR Trick:
XOR-ing a character with itself results in 0 (a ^ a = 0).
XOR-ing all characters in s and t leaves behind only the added character because all other characters cancel out.

Time Complexity: O(n)
Space Complexity: O(1)
'''