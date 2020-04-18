class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        f = []
        s = []
        
        
        for i in S:
            if i != '#':
                f.append(i)
            else:
                if f:
                    f.pop()
        
        for i in T:
            if i != '#':
                s.append(i)
            else:
                if s:
                    s.pop()
        
        p = -1
        while s and f:
            if s[p] != f[p]:
                return False
            s.pop()
            f.pop()
        
        return not s and not f
            
        