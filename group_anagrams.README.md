# Group Anagrams (LeetCode 49)

## 📌 Problem Statement
Given an array of strings `strs`, group the **anagrams** together.  
You can return the answer in **any order**.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/group-anagrams/)

# 🚀 Solution Approach
We can uniquely identify anagrams by their **character frequency counts**:
- For each string, count occurrences of each letter (`a` to `z`).
- Use this count as a tuple key in a dictionary.
- Group all words with the same key together.

✅ More efficient than sorting each string (`O(K log K)` per word).  
This approach works in **O(N · K)**, where:  
- `N` = number of words  
- `K` = maximum length of a word  

# Complexity
- **Time Complexity:** O(N · K)  
- **Space Complexity:** O(N · K)  

# 📝 Code
```python
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anagrams_dict[key].append(s)
        return list(anagrams_dict.values())
