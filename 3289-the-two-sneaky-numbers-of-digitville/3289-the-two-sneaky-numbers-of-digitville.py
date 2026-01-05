class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        r=set()
        for i in nums:
            if nums.count(i)==2:
                r.add(i)
        return list(r)