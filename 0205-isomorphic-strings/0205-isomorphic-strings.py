class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}

        # Corrected condition
        if len(set(s)) != len(set(t)):
            return False

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False

        return True
