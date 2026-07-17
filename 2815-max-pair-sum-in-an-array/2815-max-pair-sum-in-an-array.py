class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        m=-1
        for i in range(len(nums)):
            t1=nums[i]
            tm1=0
            
            while t1>0:
                r=t1%10
                tm1=max(tm1,r)
                t1=t1//10
            for j in range(i+1,len(nums)):
                t2=nums[j]
                tm2=0
                while t2>0:
                    r2=t2%10
                    tm2=max(tm2,r2)
                    t2=t2//10
                if tm1==tm2:
                    m=max(m,nums[i]+nums[j])
        return m
            
        

        