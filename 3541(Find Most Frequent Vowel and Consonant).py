class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        max_vowel_freq = 0
        max_consonant_freq = 0

        for ch, count in freq.items():
            if ch in vowels:
                max_vowel_freq = max(max_vowel_freq, count)
            else:
                max_consonant_freq = max(max_consonant_freq, count)

        return max_vowel_freq + max_consonant_freq
