from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # Step 1: BFS → shortest distance from beginWord to every reachable word
        distance = {beginWord: 0}
        graph = defaultdict(list)
        queue = deque([beginWord])
        L = len(beginWord)

        while queue:
            word = queue.popleft()
            for i in range(L):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordSet:
                        graph[word].append(new_word)
                        if new_word not in distance:
                            distance[new_word] = distance[word] + 1
                            queue.append(new_word)
            # stop BFS early once we reach endWord
            if endWord in distance and distance[word] >= distance[endWord]:
                break

        # Step 2: DFS → backtrack from beginWord to endWord using only shortest paths
        res = []
        path = [beginWord]

        def dfs(word):
            if word == endWord:
                res.append(path[:])
                return
            for nei in graph[word]:
                if distance.get(nei, float('inf')) == distance[word] + 1:
                    path.append(nei)
                    dfs(nei)
                    path.pop()

        if endWord in distance:
            dfs(beginWord)
        return res
