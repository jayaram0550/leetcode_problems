class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        l=len(colors)
        r=0
        for i in range(l):
            for j in range(l-1,-1,-1):
                if colors[i] !=colors[j]:
                    r=max(r,j-i)
                    break
        return r
    