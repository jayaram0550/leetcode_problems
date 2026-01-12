class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        d={}
        for i in stones:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in jewels:
            if i in d:
                c+=d[i]
        return c
