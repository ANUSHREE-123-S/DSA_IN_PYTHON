# Word Break (LeetCode 139)

## 📌 Problem Statement
Given a string `s` and a dictionary of strings `wordDict`,  
return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/word-break/)

# 🚀 Solution Approach
We use **Dynamic Programming**:

1. Create a boolean DP array of size `n+1`, where `dp[i]` means `s[:i]` can be segmented.  
2. Initialize `dp[0] = True` (empty string is valid).  
3. For each `i`, check all possible splits `s[j:i]`.  
   - If `dp[j]` is True and `s[j:i]` exists in the dictionary → mark `dp[i] = True`.  
4. Return `dp[n]`.  

# ⏱️ Complexity
- **Time Complexity:** `O(n^2)` (two nested loops to check substrings)  
- **Space Complexity:** `O(n)` (DP array)  

# 📝 Code
```python
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]
