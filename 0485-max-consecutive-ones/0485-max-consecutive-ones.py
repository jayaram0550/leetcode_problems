class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        j=0
        c=0
        for i in nums:
            if i==1:
                j+=1
                c=max(j,c)
            else:
                j=0
        return c


       
        