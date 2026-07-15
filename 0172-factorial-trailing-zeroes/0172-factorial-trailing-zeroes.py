class Solution:
    def trailingZeroes(self, n: int) -> int:
        a=0
        while n>0:
            n//=5
            a+=n
        return a
        