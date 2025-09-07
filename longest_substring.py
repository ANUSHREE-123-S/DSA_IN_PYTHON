class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        newset=set()
        n=len(s)
        for r in range(n):
            while s[r] in newset:
                newset.remove(s[l])
                l+=1
            w=(r-l)+1
            longest=max(longest,w)
            newset.add(s[r])
        return longest