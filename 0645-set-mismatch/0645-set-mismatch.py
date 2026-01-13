class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s=sum(set(nums))
        d=len(nums)
        n=sum(nums)
        m=d*(d+1)//2 - s
        e=n-s
        a=[]
        a.append(e)
        a.append(m)
        return a

        