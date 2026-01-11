class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d={}
        s=0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        for i in d:
            t=d[i]
            if d[i]>=2:
                s+=t*(t-1)//2
        return s

        
        