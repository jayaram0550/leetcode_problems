class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c=[]
        d=0
        for i in sentences:
            for j in i:
                if j==" ":
                    d+=1
            c.append(d)
            d=0
        return max(c)+1
            
            

        