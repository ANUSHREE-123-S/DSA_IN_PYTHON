from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet=set(wordList)
        if endWord not in wordSet:
            return 0
        L= len(beginWord)
        all_combo_dict=defaultdict(list)

        for word in wordSet:
            for i in range(L):
                pattern=word[:i]+'*'+word[i+1:]
                all_combo_dict[pattern].append(word)
        queue=deque([(beginWord,1)])
        visited=set([beginWord])

        while queue:
            word,level=queue.popleft()
            for i in range(L):
                pattern=word[:i]+'*'+word[i+1:]
                for next_word in all_combo_dict[pattern]:
                    if next_word == endWord:
                        return level+1
                    if next_word not in visited:
                        queue.append((next_word,level+1))
                all_combo_dict[pattern]=[]
        return 0