
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[]
        for i,temp in range(temperatures):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_index=stack.pop()
                ans[prev_index]=i-prev_index
            stack.append(i)
        return ans 