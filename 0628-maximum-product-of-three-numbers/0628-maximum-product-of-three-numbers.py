class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n=nums[::]
        nums.sort()
        c=0
        for i in nums:
            if i<0:
                c+=1
        if c<=1:

            return nums[-1]*nums[-2]*nums[-3]
        else:
            if c==len(n):
                return nums[-1]*nums[-2]*nums[-3]
            else:

                return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])
                

