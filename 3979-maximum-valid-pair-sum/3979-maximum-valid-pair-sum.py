class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n=len(nums)
        m=nums[0]
        a=0
        for i in range(k,n):
            m=max(m,nums[i-k])
            a=max(a,m+nums[i])
        return a
        

            