class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        c=0
        for i in range(len(s)-1,-1,-1):
            c+=1
            if s[i]==" ":
                break
        if " " not in s:
            return c
        else:
            return c-1
        