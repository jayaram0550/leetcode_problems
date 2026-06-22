class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={}
        r="balloon"
        for i in text :
            if i in r:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
        for i in r:
            if i not in d:
                return 0
        return min(d["b"],d["a"],d["l"]//2,d["o"]//2,d["n"])
         
        
                
        
        