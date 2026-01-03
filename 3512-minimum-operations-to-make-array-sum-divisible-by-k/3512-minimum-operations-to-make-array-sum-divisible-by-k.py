class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a=sum(nums)
        c=0
        for i in range(a):
            if a%k==0:
                break
            a-=1
            c+=1
        return c

        