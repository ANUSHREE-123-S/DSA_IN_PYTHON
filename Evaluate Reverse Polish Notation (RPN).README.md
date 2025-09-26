# 🔢 Evaluate Reverse Polish Notation (RPN) (LeetCode 150)

## 📌 Problem Statement
You are given an array of strings `tokens` that represents an arithmetic expression in **Reverse Polish Notation (RPN)**.  

Evaluate the expression and return an integer.  

### Valid Operators:
- `+` → Addition  
- `-` → Subtraction  
- `*` → Multiplication  
- `/` → Division (truncate toward zero)  

🔗 [LeetCode Problem Link](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

# 🚀 Approach

We use a **stack** to evaluate the postfix (RPN) expression.

# Algorithm:
1. Traverse each token in the `tokens` list:
   - If it's a **number**, push it onto the stack.  
   - If it's an **operator**:
     - Pop the **two most recent numbers** from the stack (`a` and `b`).  
     - Apply the operator:  
       - `a + b`  
       - `a - b`  
       - `a * b`  
       - `int(a / b)` (integer division truncating toward zero).  
     - Push the result back onto the stack.  
2. After processing all tokens, the stack will contain a single value → the final result.  

# ⏱️ Complexity Analysis
- **Time Complexity** → `O(n)` (process each token once)  
- **Space Complexity** → `O(n)` (stack usage)  

---

## 📝 Python Code

```python
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))  # truncates toward zero
        return stack[-1]
