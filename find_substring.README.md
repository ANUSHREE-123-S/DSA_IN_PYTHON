# Substring with Concatenation of All Words (LeetCode 30)

## 📌 Problem Statement
You are given a string `s` and an array of words `words`, all of the same length.  
Return all the starting indices of substring(s) in `s` that is a concatenation of each word in `words` **exactly once and without any intervening characters**.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

# 🚀 Solution Approach
1. Let `word_len` = length of each word, and `total_len` = total concatenation length.
2. Precompute a `Counter` (hash map) for `words`.
3. Slide a window of size `total_len` over `s`.
4. Partition the substring into chunks of size `word_len`.
5. Compare the frequency of chunks with the target `word_map`.
6. If they match, record the starting index.

# ⏱️ Complexity
- **Time Complexity:** `O(n * m)`  
  where `n = len(s)` and `m = len(words)`  
- **Space Complexity:** `O(m)` for storing word frequency map.

# 📝 Code
```python
from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_map = Counter(words)
        res = []
        for i in range(len(s) - total_len + 1):
            substring = s[i:i + total_len]
            seen = [substring[j:j + word_len] for j in range(0, total_len, word_len)]
            if Counter(seen) == word_map:
                res.append(i)
        return res
