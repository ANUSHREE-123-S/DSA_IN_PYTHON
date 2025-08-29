class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curr_max=curr_min=1
        for n in nums:
            temp=curr_max*n
            curr_max=max(temp,curr_min*n,n)
            curr_min=min(temp,curr_min*n,n)
            res=max(res,curr_max)
        return res