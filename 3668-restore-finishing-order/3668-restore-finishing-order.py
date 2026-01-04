class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        r=[]
        for i in order:
            if i in friends:
                r.append(i)
        return r