class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p=-1
        for i in range(len(nums)):
            if nums[i]==target:
                p=i
                break
        return p

        