class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)
        visited=set()
        completed=set()
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
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True