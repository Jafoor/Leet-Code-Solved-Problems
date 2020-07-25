from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        S = Counter(s)
        T = Counter(t)
        
        for key, value in T.items():
            if key not in S.keys():
                return key
            elif value != S[key]:
                return key