class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        r=[]
        for i in nums:
            c=0
            for j in range(len(nums)):
                if nums[j]<i:
                    c+=1
            r.append(c)
        return r

        