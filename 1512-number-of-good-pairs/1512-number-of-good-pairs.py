class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        #a=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j] and i<j:
                    c+=1
                    #a.append([nums[i],nums[j]])
        return c
        