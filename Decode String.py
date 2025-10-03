class Solution:
    def decodeString(self, s: str) -> str:
        numstack=[]
        strstack=[]
        currstr=""
        currnum=0
        for ch in s:
            if ch.isdigit():
                currnum=currnum*10+int(ch)
            elif ch=="[":
                numstack.append(currnum)
                strstack.append(currstr)
                currnum=0
                currstr=""
            elif ch=="]":
                repeatetimes=numstack.pop()
                prevstr=strstack.pop()
                currstr=prevstr+currstr*repeatetimes
            else:
                currstr+=ch
        return currstr

        