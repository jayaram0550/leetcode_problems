class Solution:
    def longestBalanced(self, s: str) -> int:
        pireltonak = s
        n = len(pireltonak)
        ans = 0
        for i in range(n):
            freq = {}
            for j in range(i, n):
                freq[pireltonak[j]] = freq.get(pireltonak[j], 0) + 1
                if len(set(freq.values())) == 1:
                    ans = max(ans, j - i + 1)
        return ans
