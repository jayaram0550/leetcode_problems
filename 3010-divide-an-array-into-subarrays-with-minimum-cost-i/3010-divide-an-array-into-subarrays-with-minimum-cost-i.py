class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        

        n = len(nums)
        ans = float('inf')

        # first cut at i, second cut at j
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                cost = nums[0] + nums[i + 1] + nums[j + 1]
                ans = min(ans, cost)

        return ans

        