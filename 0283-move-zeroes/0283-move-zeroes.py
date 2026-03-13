class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        b=[]
        n=len(nums)
        for i in range(n):
            if nums[i] !=0:
                b.append(nums[i])
        for i in range(len(nums)-len(b)):
            b.append(0)
        nums[:]=b[:]

        