class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        km={
            "type":0,
            "color":1,
            "name":2
        }
        c=0
        idx=km[ruleKey]
        for i in items:
            if i[idx]==ruleValue:
                c+=1
        return c
