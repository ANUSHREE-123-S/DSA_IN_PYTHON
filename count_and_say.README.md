# Count and Say (LeetCode 38)

## 📌 Problem Statement
The **count-and-say sequence** is a sequence of digit strings defined recursively:

- `"1"` is the first term.
- To generate the next term, read the previous term aloud:
  - Count the number of digits in a group.
  - Say the digit.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/count-and-say/)

# 🚀 Solution Approach
We build the sequence iteratively:
1. Start with `"1"`.
2. For each step, read the previous sequence:
   - Group consecutive digits.
   - Record `<count><digit>` in the result string.
3. Repeat this process until the `n`-th sequence.

# Complexity
- **Time Complexity:** O(n * m), where `m` is the length of the sequence.  
- **Space Complexity:** O(m), storing the sequence at each step.  

# 📝 Code
```python
class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            prev_seq = result
            result = ""
            count = 1
            for i in range(len(prev_seq)):
                if i + 1 >= len(prev_seq) or prev_seq[i] != prev_seq[i + 1]:
                    result += str(count) + prev_seq[i]
                    count = 1
                else:
                    count += 1
        return result
