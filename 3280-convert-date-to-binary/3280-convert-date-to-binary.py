class Solution:
    def convertDateToBinary(self, date: str) -> str:
        s=date.split("-")
        a=[]
        for i in s:
            a.append(bin(int(i))[2:])
            
        return "-".join(a)
        
        