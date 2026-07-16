class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        s=0
        for i in range(n):
            s=s*10+digits[i]
        s=s+1
        a=[]
        while s>0:
            r=s%10
            a.append(r)
            s=s//10
        
        return a[::-1]



        
