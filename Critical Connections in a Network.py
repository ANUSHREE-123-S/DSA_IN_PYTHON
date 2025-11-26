from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph=defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        time=0
        low=[-1]*n
        disc=[-1]*n
        res=[]
        def dfs(u,parent):
            nonlocal time
            disc[u]=low[u]=time
            time+=1

            for v in graph[u]:
                if v == parent:
                    continue
                if disc[v]==-1:
                    dfs(v,u)
                    low[u]=min(low[u],low[v])
                    if low[v]>disc[u]:
                        res.append([u,v])
                else:
                    low[u]=min(low[u],disc[v])
        dfs(0,-1)
        return res
    