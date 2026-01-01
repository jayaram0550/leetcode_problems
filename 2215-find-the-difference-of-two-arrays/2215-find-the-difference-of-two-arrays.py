class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=[]
        b=[]
        for i in nums1:
            if i not in nums2:
                a.append(i)
        for j in nums2:
            if j not in nums1:
                b.append(j)
        return (list(set(a)),list(set(b)))

        