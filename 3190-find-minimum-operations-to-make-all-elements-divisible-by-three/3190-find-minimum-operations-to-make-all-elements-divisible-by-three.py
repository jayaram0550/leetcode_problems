class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if (i%3)>3//2:
                c+=(3-(i%3))
            else:
                c+=(i%3)
        return c
            
        