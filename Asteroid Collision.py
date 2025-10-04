from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for ast in asteroids:
            alive =True
            while stack and ast<0<stack[-1]:
                if stack[-1]<-ast:
                    stack.pop()
                    continue
                elif stack[-1]==-ast:
                    stack.pop()
                alive=False
                break
            if alive:
                stack.append(ast)
        return stack