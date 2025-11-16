class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph={i:[] for i in range(numCourses)}
        for course,pre in prerequisites:
            graph[pre].append(course)
        
        visited=set()
        completed=set()
        result=[]

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