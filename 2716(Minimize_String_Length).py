class Solution:
    def minimizedStringLength(self, s: str) -> int:
        seen = {}
        result = []

        for char in s:
            if char not in seen:
                seen[char] = True
                result.append(char)
            # else: skip it (simulate removing the duplicate)

        return len(result)
    
    
"""class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
        
"""
