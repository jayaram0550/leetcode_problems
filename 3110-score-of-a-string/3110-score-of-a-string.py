class Solution:
    def scoreOfString(self, s: str) -> int:
        n=[]
        sum=0
        for ch in s:
            n.append(ord(ch)-ord('a'))
        for i in range(len(n)-1):
            sum+=abs(n[i]-n[i+1])
        return sum
        