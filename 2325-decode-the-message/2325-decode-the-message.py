class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d={}
        temp=97
        for i in key:
            if i !=" " and i not in d:
                d[i]=chr(temp)
                temp+=1
        s=""
        for i in message:
            if i !=" ":
                s+=d[i]
            else:
                s+=" "
        return s
