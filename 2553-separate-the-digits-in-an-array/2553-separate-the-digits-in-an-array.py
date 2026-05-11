class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        a=[]
        r=0
        for i in nums:
            b=[]
            while i>=10:
                r=i%10
                b.append(r)
                i=i//10
            a.append(i)
            a+=(b[::-1])
            
        return a
        