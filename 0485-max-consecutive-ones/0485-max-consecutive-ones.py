class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        cm=0
        i=0
        for i in range(len(nums)):
            if nums[i]==1:
                i=i
                break
        
        
        while i<len(nums) and nums[i]>0:
            cm+=1
            m=max(m,cm)
            i+=1
            if i<len(nums) and nums[i]==0 :
                while i<len(nums) and nums[i]==0 :
                    i+=1
                cm=0
        return m


            

        


       
        