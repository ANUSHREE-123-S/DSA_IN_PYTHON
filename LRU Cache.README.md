# LRU Cache (LeetCode 146)

# 📌 Problem Statement
Design a data structure that follows the **Least Recently Used (LRU)** cache policy.

- `get(key)` → return value if key exists, else `-1`.
- `put(key, value)` → insert/update the key-value pair.  
  If capacity is reached, evict the **least recently used** item.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/lru-cache/)

# Example 1:
```python
cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # 1

cache.put(3, 3)      # evicts key 2
print(cache.get(2))  # -1

cache.put(4, 4)      # evicts key 1
print(cache.get(1))  # -1
print(cache.get(3))  # 3
print(cache.get(4))  # 4
Approach
```
Data Structures Used:

HashMap (Dictionary): key → Node mapping for O(1) access.

Doubly Linked List: Maintains order of usage:

head → Most Recently Used (MRU)

tail → Least Recently Used (LRU)

Main Operations:

Move Node to Front: Mark a node as MRU.

Add Node: Insert a new node right after the head.

Evict Node: Remove node before tail when capacity exceeded.

Get: Return value and move node to front if exists.

Put: Add/update node and move to front; evict LRU if needed.

Why Doubly Linked List?

Supports O(1) insertion and removal from both ends and the middle, which is essential for maintaining LRU order efficiently.
