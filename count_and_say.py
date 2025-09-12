class Solution:
    def countAndSay(self, n: int) -> str:
        result="1"
        for _ in range(n-1):
            prev_seq=result
            result=""
            count=1
            for i in range(len(prev_seq)):
                if i+1>=len(prev_seq)or prev_seq[i]!=prev_seq[i+1]:
                    result+=str(count)+prev_seq[i]
                    count=1
                else:
                    count+=1
        return result