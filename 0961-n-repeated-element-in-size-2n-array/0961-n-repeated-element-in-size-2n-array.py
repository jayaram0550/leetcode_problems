class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums.count(nums[i])>=2:

                return nums[i]
                break
        