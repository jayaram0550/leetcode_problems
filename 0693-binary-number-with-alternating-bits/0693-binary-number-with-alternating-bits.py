class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        c = bin(n)[2:]   # binary string
        
        for i in range(1, len(c)):
            if c[i] == c[i-1]:
                return False
        
        return True
