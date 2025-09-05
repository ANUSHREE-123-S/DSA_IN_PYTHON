# Valid Anagram (LeetCode 242)

## 📌 Problem Statement
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.  

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.  

🔗 [LeetCode Problem Link](https://leetcode.com/problems/valid-anagram/)

# 🚀 Solution Approach
- Convert both strings into lists of characters.
- Sort both lists.
- If the sorted versions are equal → `t` is an anagram of `s`.

- **Time Complexity:** O(n log n)  
- **Space Complexity:** O(1) (ignoring sorting space)

# 📝 Code
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)
        a.sort()
        b.sort()
        return a == b
