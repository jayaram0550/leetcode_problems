class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}

        for i in range(len(nums)):
            r=target-nums[i]
            if r not in d:
                d[nums[i]]=i
            else:
                return [d[r],i]
        















        