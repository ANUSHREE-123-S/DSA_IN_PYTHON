class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        curr=0
        row=[""]*numRows
        down=False
        for char in s:
            row[curr]+=char
            if curr==0 or curr==numRows-1:
                down =not down
            curr+=1 if down else -1
        return "".join(row)