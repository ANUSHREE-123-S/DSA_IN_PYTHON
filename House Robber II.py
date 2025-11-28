class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        def rob_linear(arr):
            rob1,rob2=0,0
            for money in arr:
                newrob=max(rob2,rob1+money)
                rob1=rob2
                rob2=newrob
            return rob2
        case1=rob_linear(nums[:-1])
        case2=rob_linear(nums[1:])
        return max(case1,case2)
