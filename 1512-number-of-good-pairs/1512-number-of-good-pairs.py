class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                c+=d[i]
                d[i]+=1
        return c

        
        