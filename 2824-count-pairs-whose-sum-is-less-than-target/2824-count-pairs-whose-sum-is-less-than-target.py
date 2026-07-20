class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        c=0
        nums.sort()
        l,r=0,len(nums)-1
        while(l<r):
            s=nums[l]+nums[r]
            if s<target:
                c+=r-l
                l+=1
            else:
                r-=1
        return c
        
        