import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # Normalize: lowercase and replace punctuations with space
        paragraph = paragraph.lower()
        words = re.findall(r'\w+', paragraph)  # \w+ matches alphanumeric words
        
        banned_set = set(banned)
        word_counts = Counter(word for word in words if word not in banned_set)
        
        # Return the most common word
        return word_counts.most_common(1)[0][0]

# Copy code in chatgpt
