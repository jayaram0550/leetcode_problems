class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        s=0
        for i in range(n):
            if i%2==0:
                s+=nums[i]
        return s
