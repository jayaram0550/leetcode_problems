class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        if len(set(s)) != len(set(t)):
            return False
        else:
            for i in range(len(t)):
                ch=s[i]
                if ch not in d:
                    d[ch]=t[i]
            c=0
            for i in range(len(t)):
                if t[i]==d[s[i]]:
                    c+=1
            if c==len(t):
                return True
            else:
                return False

        

        