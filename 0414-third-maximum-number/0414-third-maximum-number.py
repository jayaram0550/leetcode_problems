class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        s=set()
        m=max(nums)
        c=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] not in s:
                s.add(nums[i])
                c+=1
                if c==3 :
                    m=nums[i]
                    break
        return m
                

        