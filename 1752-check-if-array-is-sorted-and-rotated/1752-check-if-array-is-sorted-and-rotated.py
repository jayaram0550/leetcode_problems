class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        x=0
        for i in range(n-1):
            if nums[i]>nums[i+1]: 
                x=i
                break
        if sorted(nums)==nums[x+1:]+nums[:x+1] or sorted(nums)==nums:
            return True
        else:
            return False  