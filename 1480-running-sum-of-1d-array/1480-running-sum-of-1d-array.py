class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[]
        cs=0
        for i in nums:
            cs+=i
            a.append(cs)
        return a