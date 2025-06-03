"""from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        queue=deque()
        queue.append((beginWord,1))
        while len(queue)!=0:
            curr_word,level=queue.popleft()
            if curr_word==endWord:
                return level
            for i in range(0,len(curr_word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch==curr_word[i]:
                        continue
                    new_word=curr_word[:i]+ch+curr_word[i+1:]
                    if new_word in wordset:
                        queue.append ((new_word,level+1))
                        wordset.remove(new_word)
        return 0


        """

from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if word[i] == c:
                        continue
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        queue.append((next_word, steps + 1))

        return 0
