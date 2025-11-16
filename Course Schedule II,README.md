Course Schedule II – Topological Sort (LeetCode 210)

This repository contains a Python solution to Course Schedule II, where the goal is to return a valid order of courses to finish all subjects based on prerequisites.

🧠 Problem Summary

You are given:

numCourses — total number of courses labeled 0 to numCourses - 1

prerequisites — an array of pairs [a, b] meaning you must take course b before course a

Objective

Return one valid ordering of courses you can finish OR return an empty list [] if it's impossible (i.e., there is a cycle).

This is a classic Topological Sorting problem on a directed graph.

🚀 Approach

This solution uses DFS-based Topological Sort with cycle detection.

🔑 Key Concepts:

Build a directed graph where edges represent prerequisites.

Maintain:

visited: courses currently in the recursion stack

completed: courses already fully processed

result: topologically sorted courses

If a cycle is detected → return [].

Otherwise, return the reversed result list.

🧩 Code Implementation
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[pre].append(course)

        visited = set()
        completed = set()
        result = []

        def dfs(course):
            if course in visited:
                return False
            if course in completed:
                return True

            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            completed.add(course)
            result.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return result[::-1]

✔️ Time & Space Complexity
Complexity	Explanation
Time: O(V + E)	Visit each node and its edges once
Space: O(V + E)	Graph, recursion stack, result list
🧪 Example
Input:
numCourses = 4
prerequisites = [[1,0], [2,0], [3,1], [3,2]]

Possible Output:
[0, 2, 1, 3]


(Other valid orders may exist.)

📚 Concepts Used

Directed Graphs

Depth-First Search (DFS)

Topological Sorting

Cycle Detection
