from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)
        for src,dest in tickets:
            heapq.heappush(graph[src],dest)
        route=[]
        def dfs(airport):
            while graph[airport]:
                next_dest=heapq.heappop(graph[airport])
                dfs(next_dest)
            route.append(airport)
        dfs("JFK")
        return route[::-1]
