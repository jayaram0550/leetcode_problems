class Solution:
    def reverseDegree(self, s: str) -> int:
        a = 0
        for i in range(len(s)):
            ch=s[i]
            a += (ord('z') - ord(ch) + 1) * (i+1)
        return a
