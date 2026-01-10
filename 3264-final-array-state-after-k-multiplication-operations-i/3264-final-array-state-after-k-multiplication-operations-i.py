class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
     
        n=len(nums)
        for i in range(k):
            b=nums.index(min(nums))
            nums[b]=nums[b]*multiplier
            
        return nums

        