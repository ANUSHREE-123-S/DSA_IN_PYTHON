# 🌳 Serialize and Deserialize Binary Tree

## 🧩 Problem Description
Design an algorithm to **serialize** and **deserialize** a binary tree.

- **Serialization:** Convert a binary tree into a single string representation.
- **Deserialization:** Convert that string back to the original binary tree structure.

The serialized data should represent the structure **uniquely** so that deserialization reconstructs the exact same tree.

**Deserialized Output:**  
Binary tree reconstructed exactly as above.

# 💡 Approach — Preorder DFS Traversal

We use **Depth-First Search (DFS)** (Preorder Traversal: `Root → Left → Right`) to encode and decode the binary tree.

# 🧱 Serialization Steps:
1. Traverse the tree using DFS.
2. If a node is `None`, append `"N"` (for Null) to represent an empty child.
3. Otherwise, record the node’s value.
4. Join all recorded values with commas.

# 🧩 Deserialization Steps:
1. Split the serialized string into a list of values.
2. Use recursion with an index pointer to rebuild the tree:
   - If the current value is `"N"`, return `None`.
   - Otherwise, create a node and recursively build its left and right children.


# ✅ Code Implementation

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        values = data.split(",")
        self.i = 0

        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
