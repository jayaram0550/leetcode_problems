class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        b=bin(n)[2:]
        if n>0 and b.count("1")==1:
            return True
        else:
            return False
        