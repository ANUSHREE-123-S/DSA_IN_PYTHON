class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]

        def is_palindrome(sub):
            return sub==sub[::-1]
        def backtrack(start):
            if start==len(s):
                res.append(path[:])
                return

            for end in range(start+1,len(s)+1):
                substring=s[start:end]

                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end)
                    path.pop()
        backtrack(0)
        return res