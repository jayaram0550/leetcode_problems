class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m=0
        cs=0
        for i  in gain:
            cs+=i
            m=max(m,cs)
        return m        