from typing import List

class Solution:
    def checkIfPrerequisite(self, n: int,
                            prerequisites: List[List[int]],
                            queries: List[List[int]]) -> List[bool]:
        is_prereq=[[False]*n for _ in range(n)]
        for u,v in prerequisites:
            is_prereq[u][v]=True
        for k in range(n):
            for i in range(n):
                if not is_prereq[i][k]:
                    continue
                for j in range(n):
                    if is_prereq[k][j]:
                        is_prereq[i][j]=True
        result=[]
        for u,v in queries:
            result.append(is_prereq[u][v])
        return result