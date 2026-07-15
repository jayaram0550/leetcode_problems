class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        es=0
        os=0
        for i in range(1,n+1):
            es+=i
        es=es*2
        for i in range(1,2*n,2):
            os+=i
        r=es%os
        if r==0:
            return os
        while r>0:
            r=es%os
            es=os
            os=r
        return es
        