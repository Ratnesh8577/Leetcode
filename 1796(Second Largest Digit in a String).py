class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()

        for ch in s:
            if ch.isdigit():
                digits.add(int(ch))
        
        sorted_digits = sorted(digits, reverse=True)

        return sorted_digits[1] if len(sorted_digits) >= 2 else -1
