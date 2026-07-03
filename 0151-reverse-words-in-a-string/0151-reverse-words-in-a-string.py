class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        s=s.split()
        r=""
        for i in range(len(s)-1,-1,-1):
            r+=s[i]+" "
        r=r.strip()
        return r
        