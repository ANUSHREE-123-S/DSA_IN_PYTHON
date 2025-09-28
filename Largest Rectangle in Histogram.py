class Solution:
    def largestRectangleArea(self, heights):
        stack=[]
        max_area=0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]]>h:
                height=heights[stack.pop()]
                width=i if not stack else i-stack[-1]-1
                max_area=max(max_area,height*width)
            stack.append(i)
        n=len(heights)
        while stack:
            height=heights[stack.pop()]
            width=n if not stack else n-stack[-1]-1
            max_area=max(max_area,height*width)
        return max_area