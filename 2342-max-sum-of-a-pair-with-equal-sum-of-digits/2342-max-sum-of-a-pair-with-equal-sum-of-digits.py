from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)

        for num in nums:
            t = num
            s = 0

            while t > 0:
                s += t % 10
                t //= 10

            d[s].append(num)

        ans = -1

        for arr in d.values():
            if len(arr) >= 2:
                arr.sort()
                ans = max(ans, arr[-1] + arr[-2])

        return ans