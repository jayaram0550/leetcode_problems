class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for num in nums1:
            for j in range(len(nums2)):
                if num == nums2[j]:
                    found = -1

                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > num:
                            found = nums2[k]
                            break

                    ans.append(found)
                    break

        return ans