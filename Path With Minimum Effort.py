import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols=len(heights),len(heights[0])
        efforts=[[float('inf')]*cols for _ in range(rows)]
        efforts[0][0]=0

        minHeap=[(0,0,0)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        while minHeap:
            effort,x,y=heapq.heappop(minHeap)
            if x== rows-1 and y==cols-1:
                return effort
            for dx,dy in directions:
                nx,ny=x+dx,y+dy

                if 0<=nx <rows and 0<= ny <cols:
                    currEffort = abs(heights[nx][ny]-heights[x][y])
                    maxEffort=max(effort,currEffort)

                    if maxEffort < efforts[nx][ny]:
                        efforts[nx][ny]=maxEffort
                        heapq.heappush(minHeap,(maxEffort,nx,ny))
        return 0
            