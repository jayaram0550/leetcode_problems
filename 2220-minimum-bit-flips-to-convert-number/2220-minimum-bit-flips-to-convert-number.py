class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        b=bin(start)[2:].zfill(32)
        c=bin(goal)[2:].zfill(32)
        d=0
        for i in range(len(b)):
            if b[i]!=c[i]:
                d+=1
        return d

        