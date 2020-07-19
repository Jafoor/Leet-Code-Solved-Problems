class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        d = {}
        
        for (ltr1, ltr2) in zip(s,t):
            
            if ltr1 not in d.keys():
                if ltr2 in d.values():
                    return False
                else:
                    d[ltr1] = ltr2
            elif d[ltr1] != ltr2:
                return False
        return True