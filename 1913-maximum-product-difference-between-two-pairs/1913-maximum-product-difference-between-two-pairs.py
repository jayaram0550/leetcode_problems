class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        m1=nums[-1]*nums[-2]
        l1=nums[0]*nums[1]
        return m1-l1